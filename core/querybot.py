import requests
import core.apitokenpool as pool


class QueryBot(object):
    __id = None
    __session = None
    __token_pool = None

    def __init__(self):
        self.__id = None
        self.__session = requests.Session()
        self.__token_pool = pool.ApiTokenPool()

    # 执行查询
    def query(self, question: str) -> str:
        api_token = self.__token_pool.get()
        print(api_token)
        response = requests.post(url="https://api.openai.com/v1/chat/completions",
                                 headers={
                                     'Content-Type': 'application/json',
                                     'Authorization': f'Bearer {api_token}'
                                 },
                                 json={
                                     'model': 'gpt-3.5-turbo',
                                     'messages': [{'role': 'assistant', 'content': question}],
                                     'stream': False,
                                     'temperature': 0.7,
                                 },
                                 stream=False, )
        return response.content.decode('utf-8')

    # 获取历史查询记录
    def load_history(self):
        pass
