import json

import requests

question = "帮我把下面的短文做个摘要，短文：我是最不受这种激情折磨的人之一，尽管社会已经同意以公正的报酬来表彰她的特殊恩宠，但我对她没有任何爱好或热爱；在世界上，智慧，美德，良心都被掩饰了；丑陋而愚蠢的装饰品..."
response = requests.post(url="https://api.openai.com/v1/chat/completions",
                         headers={
                             "Content-Type": "application/json",
                             "Authorization": "Bearer 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",
                         },
                         json={
                             "model": "gpt-3.5-turbo",
                             "messages": [{"role": "user", "content": question}],
                             "stream": False,
                             # kwargs
                             "temperature": 0.7,
                             # "top_p": kwargs.get("top_p", self.top_p),
                             # "n": kwargs.get("n", self.reply_count),
                             # "user": "user",
                         },
                         stream=True, )
print(question)
full_response_json = json.loads(response.content.decode("utf-8"))
print(full_response_json['choices'])