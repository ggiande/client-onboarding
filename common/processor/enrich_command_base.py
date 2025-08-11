from common.processor.command_abc import CommandABC
from abc import ABC, abstractmethod

class EnrichCommandBase(CommandABC):

    def __init__(self, service_name: str):
        self.service_name = service_name
        self.command_name = "EnrichCommandBase"

    def post_process(self) -> None:
        pass

    def handle_exception(self) -> None:
        pass

    def handle_command_execution_exception(self) -> None:
        pass

    def is_telemetry_turned_on(self) -> bool:
        return False

    def get_event_region_name(self) -> str:
        pass

    @abstractmethod
    def is_command_applicable(self) -> bool:
        return False

    @abstractmethod
    def execute(self, data: dict) -> None:
        pass

