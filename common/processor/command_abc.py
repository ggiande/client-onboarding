"""Abstract Base Class"""
from abc import ABC, abstractmethod

class CommandABC(ABC):
    """Interface for the command pattern

    Args:
        ABC (_type_): Inherits obj of an abstract base class

    Returns:
        _type_: None
    """

    @abstractmethod
    def execute(self, data: dict) -> None:
        """Execute a command

        Args:
            data (dict): map passing data, obj request_context
        """
        pass

    @abstractmethod
    def handle_exception(self) -> None:
        pass

    @abstractmethod
    def handle_command_execution_exception(self) -> None:
        pass

    @abstractmethod
    def is_telemetry_turned_on(self) -> bool:
        return False

    @abstractmethod
    def get_event_region_name(self) -> str:
        return ""

    @abstractmethod
    def post_process(self) -> None:
        pass

    @abstractmethod
    def is_command_applicable(self) -> bool:
        return False
