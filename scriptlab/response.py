import json

# TODO: add validation pls
class RunDetails:
    
    def __init__(self, req: dict):
        
        self.exit_code = req['exit_code']
        self.error = req['error']
        self.logs = req['logs']
        self.response = req['response']
        self.output = req['output']


class Response:

    def __init__(self, rd: RunDetails):
        self.__rd__ = rd

    def exit_code(self) -> int:
        return self.__rd__.exit_code

    def error(self) -> str:
        return self.__rd__.error

    def logs(self) -> list:
        return self.__rd__.logs

    def stdout(self) -> list:
        return self.__rd__.output

    def response(self) -> str:
        return self.__rd__.response

    def json(self) -> dict:
        return json.loads(self.__rd__.response)
        

class ActionResponse(Response):

    def __init__(self, rd: RunDetails):
        super().__init__(rd)


class CommandResponse(Response):

    def __init__(self, rd: RunDetails):
        super().__init__(rd)
        