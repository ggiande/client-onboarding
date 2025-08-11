from typing import List

from common.processor import CommandABC

class Invoker:
    def __init__(self):
        self._commands: List[CommandABC] = []

    def add_command(self, command: CommandABC):
        self._commands.append(command)

    def run_all(self) -> List:
        results = []
        for command in self._commands:
            res = command.execute()
            results.append(res)
        self._commands.clear() # clear the list after execution
        return results
