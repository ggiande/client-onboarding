from request.processor.command import Command

class RequestDataEnrichCommand(Command):

    def __init__(self, service_name: str):
        self.service_name = service_name

    def execute(self, data: dict):
        print(f"Getting status for service: {self.service_name}")
        # Add your logic to get the service status here
        return {"status": "success", "message": f"Service '{self.service_name}' is running."}

    def post_process(self):
        pass

    def get_event_region_name(self):
        pass

    def is_telemetry_turned_on(self):
        pass

    def handle_command_execution_exception(cls):
        pass

    def handle_exception(self):
        pass

