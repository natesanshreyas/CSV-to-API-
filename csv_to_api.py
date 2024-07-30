import pandas as pd
import requests
import json
import time

def csv_to_api():
    
    df = pd.read_csv('./seeding.csv') #converting PDF to dataframe, making it easier to read
    df.columns = df.columns.str.strip() #preventing whitespace from throwing off results

    token = '' #access token, used to authenticate into API. Make sure to replace this with the access token that you generate following the instructions in the Readme
    key = '' #API key, used to authenticate into API

    headers = { #converting token and key into headers 'X-API-Access-Token' and 'X-API-Key'. It's necessary to seperate out the headers in this format in order to successfully make the API call
        'X-API-Access-Token': token,
        'X-API-Key': key
        }

    url = 'https://soedemo.stackenterprise.co/api/2.3/questions/add'  #SOE URL leveraging API 2.3. Make sure to replace 'soedemo' with the name of your instance

    for index in range(len(df)): #Pulling out each row of the CSV
        data = df.loc[index]
        print(data)        
   
        payload = { #Mapping API parameters ('title','body', 'tags') to column headers in the CSV
            'title': data['Title'],
            'body': data['Body'],
            'tags': data['Tags'],
            'preview': False #Posts questions directly to the instance
        }

        print(headers)
        print(payload)

        while True:


            response = requests.post(url, params=payload, headers=headers, proxies=None) #POST request 
            data = json.loads(response.text) #Retrieves the response text and converts into a coresponding Python object, then assigns the object to variable "data"
                

            if response.status_code == 400 and response.json().get('backoff'): #POSTing to API 2.3 necessitates a 60 second wait between each successive POST. 
                                                                                #This code block ensures that the next POST happens 60 seconds after the first one
                                                                                #The API response will be a 400 if the "backoff" key is triggered by a second POST
                backoff_time = response.json().get('backoff') #returns a Python object representing the JSON data for the "backoff" key from the API
                print(f"API Backoff request received. Waiting {backoff_time} seconds...")
                time.sleep(backoff_time) #Waits the specified backoff time (60 seconds) before POSTing again
                continue

            elif response.status_code != 200: #If the error message is not a 400, this code block will print the response for the error message and the details of the error
                print(f"API call failed with status code: {response.status_code}.")
                print(response.text)
                break

            else:  #If the POST is successful, the question_IDs for the posted questions will then be sent to the original CSV file. 
                    #This is needed for answers to be POSTed as well
                items = data["items"]
                question_ids = [item["question_id"] for item in items]
                print (response.text)
                print('POST request successful')
                print (f'The question id"s are {question_ids}')

                df.at[index, 'Question ID'] = question_ids[0]

                break


    df.to_csv('./seeding.csv', index=False)

csv_to_api()
