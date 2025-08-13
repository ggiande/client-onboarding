from common.processor.event_task_command_abc import EventTaskCommandBaseABC
from request.processor import RequestInitializeCommand, RequestDataValidateCommand, RequestTransformCommand, \
    RequestSaveCommand, RequestMockCommand
from request.processor.request_data_enrich_command import RequestDataEnrichCommand
from sqlalchemy.orm import Session

# Invoker
class RequestEventTaskCommand(EventTaskCommandBaseABC):
    def __init__(self, service_name: str):
        super().__init__(service_name)
        self._commands = [
            RequestInitializeCommand(self.service_name),
            RequestDataValidateCommand(self.service_name),
            RequestDataEnrichCommand(self.service_name),
            RequestTransformCommand(self.service_name),
            RequestSaveCommand(self.service_name),
            RequestMockCommand(self.service_name)
        ]

    def execute(self, data: dict, db_session: Session) -> dict:
        print(f"Executing {self.__class__.__name__} for service {self.service_name}")

        print("Starting a sequence of commands...")
        current_data = data.copy() # Work on a copy to avoid side effects

        for command in self._commands:
            try:
                # Execute each command and update the data with the result
                current_data = command.execute(current_data, db_session)
            except Exception as e:
                print(f"Command failed: {command.__class__.__name__} with error: {e}")
                # You can add error handling or a rollback mechanism here
                raise e # Re-raise the exception to stop the sequence

        print("All commands executed successfully.")
        return current_data
