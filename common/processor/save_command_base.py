from abc import abstractmethod

from common.processor import CommandABC
from sqlalchemy.orm import Session


class SaveCommandBase(CommandABC):
    def post_process(self) -> None:
        pass

    @abstractmethod
    def execute(self, data: dict, db_session: Session) -> None:
        pass

    def handle_exception(self) -> None:
        pass

    def handle_command_execution_exception(self) -> None:
        pass

    def is_telemetry_turned_on(self) -> bool:
        return False

    def get_event_region_name(self) -> str:
        return ""

    def is_command_applicable(self, data: dict) -> bool:
        return data["is_applicable"]

    @abstractmethod
    def save(self) -> bool:
        pass
