import json

class ActionResponse:

    def __init__(self, status_code: int, response: str, error: str = ""):

        self.status_code = status_code
        self.response = response
        self.error = error

    def json(self) -> dict:
        return json.loads(self.response)
        