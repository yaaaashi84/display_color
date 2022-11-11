import json
import requests


url = "http://127.0.0.1:8000"

# URLからデータを取得
res = requests.get(url)

# JSON形式からパース
JSON_object = res.json()

print(JSON_object)  # {'a': 'apple', 'b': 'banana', 'c': 'cake'}
