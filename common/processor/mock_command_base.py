""""Base Class Inherits from ABC"""
from abc import abstractmethod

from common.processor import CommandABC
from sqlalchemy.orm import Session


class MockCommandBase(CommandABC):
    """
      Services Mock Command Impl CommandABC
    Args:
        CommandABC (_type_): _description_
    """

    def handle_exception(self) -> None:
        pass

    @abstractmethod
    def execute(self, data: dict, db_session: Session) -> None:
        pass

    def handle_command_execution_exception(self) -> None:
        pass

    def is_telemetry_turned_on(self) -> bool:
        return False

    def get_event_region_name(self) -> str:
        return ""

    def post_process(self) -> None:
        pass

    def is_command_applicable(self, data: dict) -> bool:
        return data.get("is_applicable")