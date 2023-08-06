import pandas as pd
import requests
import json    

def questions_get():
    key = 'RWTwPJoVDdPQy8GzMkdKsQ(('

    headers = {'X-API-Key': key}

    url = 'https://soedemo.stackenterprise.co/api/2.3/questions'

    payload = {
        'page': 1,
        'pagesize': 4,
        'fromdate': 1685577600,
        'todate': 1686700800,
        'order': 'desc',
        'min': 1685577600,
        'max': 1686700800,
        'sort': 'activity'
    }

    response = requests.get(url, params=payload, headers=headers, proxies=None)
    data = json.loads(response.text)


    print(response.status_code)
    print(response.text)

    if response.status_code == 200:
        items = data["items"]
        question_ids = [item["question_id"] for item in items]
        print('GET request successful')
        print (response.text)
        print (f'The question id"s are {question_ids}')
    else:
        print('GET request failed')
        print (response.text)

questions_get()