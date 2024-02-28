import json
from dataclasses import dataclass
from typing import Any, Iterator, NoReturn

import grpc
from numerous.grpc import spm_pb2, spm_pb2_grpc


@dataclass
class Message:
    channel: str
    message: Any

    @staticmethod
    def from_proto(message: spm_pb2.SubscriptionMessage):
        return Message(
            channel=message.channel,
            message=json.loads(message.message),
        )


class Subscription:
    def __init__(
        self,
        project_id: str,
        scenario_id: str,
        spm_stub: spm_pb2_grpc.SPMStub,
        channel_patterns: list[str],
    ):
        self._spm_stub = spm_stub
        self._stream: Iterator[
            spm_pb2.SubscriptionMessage
        ] = self._spm_stub.SubscribeForUpdates(
            spm_pb2.Subscription(
                channel_patterns=channel_patterns,
                scenario=scenario_id,
                project_id=project_id,
            )
        )  # type: ignore[assignment]

    def _handle_cancelled_if_subscription_closed(
        self, error: grpc.RpcError
    ) -> NoReturn:
        if (
            error.code() == grpc.StatusCode.CANCELLED
            and error.details() == "Channel closed!"
        ):
            raise StopIteration

        else:
            raise

    def __iter__(self) -> "Subscription":
        return self

    def __next__(self) -> Message:
        try:
            return Message.from_proto(next(self._stream))
        except grpc.RpcError as error:
            self._handle_cancelled_if_subscription_closed(error)
