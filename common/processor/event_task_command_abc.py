from typing import List

from common.processor import CommandABC


class EventTaskCommandBaseABC:

    def __init__(self, service_name: str = "DEFAULT"):
        self.service_name = service_name
        self._commands: List[CommandABC] = []
