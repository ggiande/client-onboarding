from abc import abstractmethod, ABC
from typing import List

from common.processor import CommandABC
from sqlalchemy.orm import Session

class EventTaskCommandBaseABC(ABC):

    def __init__(self, service_name: str = "DEFAULT"):
        self.service_name = service_name
        self._commands: List[CommandABC] = []

    @abstractmethod
    def execute(self, data: dict, db_session: Session) -> dict:
        pass
