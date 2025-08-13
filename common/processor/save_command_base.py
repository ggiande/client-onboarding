from abc import abstractmethod

from common.processor import CommandABC


class SaveCommandBase(CommandABC):
    def post_process(self) -> None:
        pass

    @abstractmethod
    def execute(self, data: dict) -> None:
        pass

    def handle_exception(self) -> None:
        pass

    def handle_command_execution_exception(self) -> None:
        pass

    def is_telemetry_turned_on(self) -> bool:
        return False

    def get_event_region_name(self) -> str:
        return ""

    @abstractmethod
    def is_command_applicable(self) -> bool:
        return False

    @abstractmethod
    def save(self) -> bool:
        pass
