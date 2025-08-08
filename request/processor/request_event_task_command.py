from typing import List

from request.processor import RequestInitializeCommand, RequestDataValidateCommand, RequestTransformCommand, \
    RequestSendCommand, RequestMockCommand
from request.processor.command import Command
from request.processor.request_data_enrich_command import RequestDataEnrichCommand


# Invoker
class RequestEventTaskCommand:
    def __init__(self):
        self.service_name = "FAST_API"
        self._commands = [
            RequestInitializeCommand(self.service_name),
            RequestDataValidateCommand(self.service_name),
            RequestDataEnrichCommand(self.service_name),
            RequestTransformCommand(self.service_name),
            RequestSendCommand(self.service_name),
            RequestMockCommand(self.service_name)
        ]

    def execute(self, data: dict) -> dict:
        print("Starting a sequence of commands...")
        current_data = data.copy() # Work on a copy to avoid side effects

        for command in self._commands:
            try:
                # Execute each command and update the data with the result
                current_data = command.execute(current_data)
            except Exception as e:
                print(f"Command failed: {command.__class__.__name__} with error: {e}")
                # You can add error handling or a rollback mechanism here
                raise e # Re-raise the exception to stop the sequence

        print("All commands executed successfully.")
        return current_data
