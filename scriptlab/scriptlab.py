import json
import os
import requests

from . import context

url = "http://localhost:"+os.getenv("PORT")+"/v1"

class Scriptlab:

    def __init__(self) -> None:

        # get run context
        rc = json.loads(os.getenv("RUN_CONTEXT"))
        if rc == None:
            raise Exception

        self.exec_id = rc["exec_id"] if "exec_id" in rc else None
        
        self.context = context.Context(rc["context"]) if rc["context"] else context.Context({})
        self._to_set = []
        self.context._to_set = self._set_callback
        self.context._to_delete = self._del_callback
        self.context_id = rc["context_id"]
        self.file_name = rc["file_name"]
        self.exec_env = rc["exec_env"]
        self.args = rc['args']
        self.env = rc['env']
        
        self._result_path = rc["result_path"]
        self._result = {
            "ctx_set": {},
            "ctx_del": [],
            "logs": [],
            "response": ""
        }

        self._save_result()

    def get_context(self) -> context.Context:

        return self.context

    def _set_callback(self, key: str, value: any) -> None:

        self._result["ctx_set"].update({key: value})
        self._save_result()

    def _del_callback(self, key) -> None:

        self._result["ctx_del"].append(key)
        self._save_result()

    def log(self, log:str) -> None:
        self._result["logs"].append(log.replace('\n', ''))
        self._save_result()

    def _run(self, eid: str, data: dict = {}) -> dict:

        if self.exec_id == eid:
            print("recursion it's not allowed")
            raise Exception

        res = requests.post(url + "/run/"+eid, json={
            "body": data
        })

        if res.status_code != 200:
            print(f"request error {res.status_code}")
            raise Exception

        return res.json()["details"]

    def response(self, data: str) -> None:

        if type(data) != str:
            raise TypeError

        self._result["response"] = data
        self._save_result()

    def _save_result(self) -> None:
        print(self._result)
        with open(self._result_path, '+w') as f:
            json_str = json.dumps(self._result)
            f.write(json_str)
            f.close()