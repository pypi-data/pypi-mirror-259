import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    max_status_message_length: int = 32
    min_status_update_interval_seconds: float = 1.0
    grpc_max_message_size: int = 4 * 1024 * 1024
    terminate_handler_timeout: Optional[float] = 5.0

    @staticmethod
    def from_environment():
        config = Config()
        if "MAX_STATUS_MESSAGE_LENGTH" in os.environ:
            config.max_status_message_length = int(
                os.environ["MAX_STATUS_MESSAGE_LENGTH"]
            )
        if "GRPC_MAX_MESSAGE_SIZE" in os.environ:
            config.grpc_max_message_size = int(os.environ["GRPC_MAX_MESSAGE_SIZE"])
        return config
