import pandas as pd
import requests
import json
import time

def answers_post():
    df = pd.read_csv('./seeding.csv') #converting PDF to dataframe, making it easier to read
    df.columns = df.columns.str.strip() #preventing whitespace from throwing off results


    key = 'Uk0UnDoJG1pvE1EKAZOjBA((' #API key, used to authenticate into API
    headers = {'X-API-Key': key}  #converting token and key into headers 'X-API-Access-Token' and 'X-API-Key'. It's necessary to seperate out the headers in this format in order to successfully make the API call


    for index in range(len(df)): #Pulling out each row of the CSV
        data = df.loc[index]
        print(data)

        if pd.notna(data['Question ID']):
            url_qid = int(data['Question ID'])
        else:
            # Handle the case when 'Question ID' is NaN (Not a Number)
            continue

        url = f'https://soedemo.stackenterprise.co/api/2.3/questions/{url_qid}/answers/add'

        payload = { #Mapping API parameters ('title','body', 'tags') to column headers in the CSV. 
                    #The API POST request for answers requires answer body and access token
            'body': data['Answer1'],
            'preview': False,
            'access_token': 'phvXQyeo(vbxYV7OIy3BCA))'
        }


        while True:

            response = requests.post(url, data=payload, headers=headers, proxies=None) #POSTing to API 2.3 necessitates a 60 second wait between each successive POST. 
                                                                                #This code block ensures that the next POST happens 60 seconds after the first one
                                                                                #The API response will be a 400 if the "backoff" key is triggered by a second POST

            print(response.status_code)

            if response.status_code == 400 and response.json().get('backoff'):
                backoff_time = response.json().get('backoff') #returns a Python object representing the JSON data for the "backoff" key from the API
                print(f"API Backoff request received. Waiting {backoff_time} seconds...")
                time.sleep(backoff_time) #Waits the specified backoff time (60 seconds) before POSTing again
                continue

            elif response.status_code != 200:  #If the error message is not a 400, this code block will print the response for the error message and the details of the error
                print(f"API call failed with status code: {response.status_code}.")
                print(response.text)
                break

            else: #If the POST is successful, the question_IDs for the posted questions will then be sent to the original CSV file. 
                    #This is needed for answers to be POSTed as well
                print('POST request successful')
                print(response.text)
                break

answers_post()
