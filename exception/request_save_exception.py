
class RequestSaveException(Exception):

    def __init__(self, errors: dict):
        self.errors = errors
        error_messages = ", ".join([
            f"{field}: {', '.join(messages)}"
            for field, messages in errors.items()
        ])
        super().__init__(f"Request Save Command failed: {error_messages}")
