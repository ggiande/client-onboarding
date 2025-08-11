from common.processor import EnrichCommandBase

class RequestDataEnrichCommand(EnrichCommandBase):

    def is_command_applicable(self) -> bool:
        return True

    def __init__(self, service_name: str):
        super().__init__(service_name)
        self.service_name = service_name

    def execute(self, data: dict):
        print(f"Executing {self.__class__.__name__} for service {self.service_name}")

        if not self.is_command_applicable(): return None
        print(f"Getting status for service: {self.service_name}")
        # Add your logic to get the service status here
        return {"status": "success", "message": f"Service '{self.service_name}' is running."}


    def handle_exception(self):
        pass

