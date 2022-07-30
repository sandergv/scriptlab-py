
class Context:

    def __init__(self, data: dict):
        self._data = data
        self._to_set = None # callbac
        self._to_delete = None # callback

    def set(self, key: str, value: any) -> None:

        self._data.update({key: value})
        
        if self._to_set:
            self._to_set(key, value)

    def get(self, key: str) -> any:
        return self._data[key]

    def delete(self, key):
        self._data.pop(key)
        
        if self._to_delete:
            self._to_delete(key)