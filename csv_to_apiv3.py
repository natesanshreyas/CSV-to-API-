import pandas as pd
import requests
import json
import csv


def csv_to_apiv3():

    with open('./seeding.csv', 'r') as f:
        data = csv.DictReader(f)
        data = [row for row in data]

    headers = {
        'Authorization': "Bearer LpwtEnNCi3iv2hIr8Qdiqw))",
        'Content-Type': 'application/json'
    }

    url = 'https://soedemo.stackenterprise.co/api/v3/questions'

    for content in data:
        payload = {
            'title': content['Title'],
            'body': content['Body'],
            'tags': content['Tags'].split(','),
            'preview': False
        }

        encoded_payload = json.dumps(payload).encode('utf-8')
        data_response = send_api_call(url, encoded_payload, headers)

        question_id = data_response['id']
        print(f'The question ID is {question_id}')

        print('Now posting answers...')
        post_answer(content['Answer1'], question_id, headers)
        post_answer(content['Answer2'], question_id, headers)


def post_answer(answer_body, question_id, headers):

    url = f'https://soedemo.stackenterprise.co/api/v3/questions/{question_id}/answers' 

    payload = {
        'body': answer_body,
        'preview': False,
        'access_token': 'phvXQyeo(vbxYV7OIy3BCA))'
    }

    encoded_payload = json.dumps(payload).encode('utf-8')
    data_response = send_api_call(url, encoded_payload, headers)

    print('Answer post was successful')


def send_api_call(url, payload, headers):

    headers = {
        'Authorization': "Bearer LpwtEnNCi3iv2hIr8Qdiqw))",
        'Content-Type': 'application/json'
    }

    response = requests.post(url, data=payload, headers=headers, proxies=None)
    print(response.text)
    data_response = json.loads(response.text)

    if response.status_code not in [200, 201, 204]:
        print(f"API call failed with status code: {response.status_code}.")
        print(response.text)
        raise SystemExit

    print(response.text)
    print('POST request successful')

    return data_response


csv_to_apiv3()
