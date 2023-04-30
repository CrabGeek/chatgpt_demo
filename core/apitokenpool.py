import threading


class ApiTokenPool(object):
    _instance_lock = threading.Lock()
    __pool = list()

    def __init__(self):
        pass

    def get(self) -> str:
        return self.__pool[0]

    def get_all(self) -> list:
        return self.__pool

    def set(self, tokens: list):
        self.__pool = tokens

    def __new__(cls, *args, **kwargs):
        if not hasattr(ApiTokenPool, "_instance"):
            with ApiTokenPool._instance_lock:
                if not hasattr(ApiTokenPool, "_instance"):
                    ApiTokenPool._instance = object.__new__(cls)
        return ApiTokenPool._instance

