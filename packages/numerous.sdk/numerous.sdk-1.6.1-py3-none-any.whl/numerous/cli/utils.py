import logging
import sys
import tarfile
from enum import Enum
from fnmatch import fnmatch
from hashlib import sha256
from io import BytesIO
from os import linesep
from pathlib import Path, PurePosixPath
from typing import Any, Callable, ContextManager, Generator, Iterable, Optional
from urllib.parse import urlparse
from uuid import uuid4

import grpc
from colorama import Fore, Style
from colorama import init as init_colorama
from grpc_interceptor import ClientCallDetails, ClientInterceptor
from numerous.grpc.spm_pb2_grpc import TokenManagerStub
from pathspec import PathSpec

log = logging.getLogger("__name__")


init_colorama()


def red(msg: Any) -> str:
    return f"{Fore.RED}{msg}{Fore.RESET}"


def green(msg: Any) -> str:
    return f"{Fore.GREEN}{msg}{Fore.RESET}"


def cyan(msg: Any) -> str:
    return f"{Fore.CYAN}{msg}{Fore.RESET}"


def yellow(*msg: Any, sep: str = " ") -> str:
    return f"{Fore.YELLOW}{sep.join(msg)}{Fore.RESET}"


def bold(msg: Any) -> str:
    return f"{Style.BRIGHT}{msg}{Style.NORMAL}"


def print_error_and_exit(msg: Any, exit_code: int = 1):
    print(red(msg))
    sys.exit(exit_code)


def print_repository_help_message(path: Path):
    print(
        f" ! {bold('Remember to change directory to the repository:')} {bold(cyan(f'cd {path}'))}"
    )
    print(f" * Connect a remote: {bold(cyan('numerous config --remote <REMOTE URL>'))}")
    print(
        f" * Checkout a scenario: {bold(cyan('numerous checkout --scenario <SCENARIO ID>'))}"
    )
    print(f" * Push changes: {bold(cyan('numerous push -c <COMMENT>'))}")
    print(f" * Build code and update scenario: {bold(cyan('numerous build'))}")


def get_grpc_channel(
    url: str,
    auth_plugin: Optional[grpc.AuthMetadataPlugin],
    extra_interceptors: Optional[list[ClientInterceptor]],
) -> grpc.Channel:
    parsed_url = urlparse(url)

    options = (
        ("grpc.keepalive_time_ms", 10000),
        ("grpc.keepalive_timeout_ms", 5000),
        ("grpc.keepalive_permit_without_calls", 1),
        ("grpc.http2_max_pings_without_data", 9999),
    )

    if parsed_url.scheme == "https":
        channel = grpc.secure_channel(
            f"{parsed_url.hostname}:{parsed_url.port or '443'}",
            grpc.composite_channel_credentials(
                grpc.ssl_channel_credentials(),
                grpc.metadata_call_credentials(auth_plugin),
            )
            if auth_plugin
            else grpc.ssl_channel_credentials(),
            options=options,
        )
    elif parsed_url.hostname == "localhost":
        log.debug("Getting local channel")
        channel = grpc.secure_channel(
            f"{parsed_url.hostname}:{parsed_url.port or '50056'}",
            grpc.local_channel_credentials(),
            options=options,
        )
    else:
        channel = grpc.insecure_channel(
            f"{parsed_url.hostname}:{parsed_url.port or '80'}", options=options
        )

    if extra_interceptors:
        channel = grpc.intercept_channel(channel, *extra_interceptors)

    return channel


class OrganizationInterceptor(ClientInterceptor):
    def __init__(self, organization_slug: str):
        self._organization_slug = organization_slug

    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        call_details: grpc.ClientCallDetails,
    ):
        new_metadata = (call_details.metadata or []) + [
            ("numerous-organization", self._organization_slug)
        ]

        new_details = ClientCallDetails(
            method=call_details.method,
            timeout=call_details.timeout,
            metadata=new_metadata,
            credentials=call_details.credentials,
            wait_for_ready=call_details.wait_for_ready,
            compression=call_details.compression,
        )

        return method(request_or_iterator, new_details)


class StubClient:
    def __init__(
        self,
        api_url: str,
        stub: Callable[[grpc.Channel], Any],
        plugin: Optional[grpc.AuthMetadataPlugin] = None,
        extra_interceptors: Optional[list[ClientInterceptor]] = None,
    ):
        self.channel = get_grpc_channel(api_url, plugin, extra_interceptors)
        self.stub = stub(self.channel)

    def __enter__(self):
        return self.stub

    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        self.channel.close()


def get_token_manager(
    api_url: str, organization_slug: str
) -> ContextManager[TokenManagerStub]:
    return StubClient(
        api_url,
        TokenManagerStub,
        extra_interceptors=[OrganizationInterceptor(organization_slug)],
    )


class GzippedTarball:
    def __init__(self, source: Path, paths: Iterable[Path]):
        self.source = source
        self.files = list(path for path in paths if path.is_file())
        self.tar_path = source / f"{uuid4()}.tar.gz"

    def __enter__(self):
        with tarfile.open(str(self.tar_path), mode="w:gz") as tar:
            for file_path in self.files:
                info = tarfile.TarInfo(str(PurePosixPath(Path(file_path.name))))
                info.path = str(file_path.relative_to(self.source))
                info.size = file_path.stat().st_size
                with file_path.open("rb") as file:
                    tar.addfile(info, fileobj=file)
        return self.tar_path

    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        self.tar_path.unlink()


def display_error_and_exit(
    error_header: str, help_lines: list[str], exit_code: int = 1
):
    print(red(error_header))
    print(*help_lines, sep=linesep)
    sys.exit(exit_code)


def extract_gzipped_tarball(file: BytesIO, path: Path) -> None:
    with tarfile.open(fileobj=file, mode="r:gz") as tar:
        tar.extractall(str(path))


def exclude_paths(
    root: Path,
    paths: Iterable[Path],
    exclude_patterns: list[str],
) -> Generator[Path, None, None]:
    spec = PathSpec.from_lines("gitwildmatch", exclude_patterns)
    for path in paths:
        relative_path = path.relative_to(root)
        exclude = spec.match_file(str(relative_path))
        if not exclude:
            yield path


def walk(directory: Path, include_pattern: Optional[str] = None):
    yield from _walk(directory, directory, include_pattern)


def _walk(
    root: Path, directory: Path, include_pattern: Optional[str] = None
) -> Generator[Path, None, None]:
    for path in directory.iterdir():
        relative_path = path.relative_to(root)
        if include_pattern and not fnmatch(str(relative_path), include_pattern):
            continue

        yield path
        if path.is_dir():
            yield from _walk(root, path, include_pattern)


def hash_directory(directory: Path) -> str:
    dirhash = sha256()
    for file_path in (path for path in walk(directory) if path.is_file()):
        dirhash.update(str(file_path.lstat().st_mtime).encode("utf-8"))
    return dirhash.hexdigest()


class RepositoryConfigLoadWarning(Enum):
    REMOTE_INVALID = 0
    PROJECT_SCENARIO_INVALID = 1
    PROJECT_SCENARIO_MISSING = 2
    COMMIT_MISSING = 3
    SNAPSHOT_MISSING = 4


def print_load_warnings(warnings: list[RepositoryConfigLoadWarning]) -> None:
    if warnings:
        print(
            yellow(
                f"{len(warnings)} where found while loading repository configuration"
            )
        )

    for warning in warnings:
        if warning == RepositoryConfigLoadWarning.COMMIT_MISSING:
            print(
                yellow(
                    bold("Commit missing:"), "Current commit will not be highlighted."
                )
            )
        elif warning == RepositoryConfigLoadWarning.PROJECT_SCENARIO_INVALID:
            print(yellow(bold("Invalid scenario:"), "Checkout needed."))
        elif warning == RepositoryConfigLoadWarning.PROJECT_SCENARIO_MISSING:
            print(yellow(bold("No scenario:"), "Checkout needed"))
        elif warning == RepositoryConfigLoadWarning.REMOTE_INVALID:
            print(
                yellow(
                    bold("Invalid remote:"),
                    "The configured remote is invalid, you must run "
                    "'numerous config --remote REMOTE' again",
                )
            )
        elif warnings == RepositoryConfigLoadWarning.SNAPSHOT_MISSING:
            print(
                yellow(
                    bold("Snapshot missing:"),
                    "No snapshot is defined, you must push with "
                    "'numerous push -c COMMENT'",
                )
            )


class NumerousCommandLineError(Exception):
    pass
