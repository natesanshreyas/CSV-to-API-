# CSV-to-API-Readme 
The purpose of this script is to enable you to automatically upload Q&A to your Stack Overflow for Teams instance from a CSV. This will help you with content seeding 
and prevent an "empty stadium" effect when your instance is created. 

There are several CSV-to-API scripts in this repo. The **csv_to_api.py ** script can post questions and answers to an instance of Stack Overflow for Teams using version 2.3 of the Stack Overflow API. Use the following steps to post Q&A to Stack Overflow for Teams **Enterprise**

1) Create an API access key in SOE. Make note of the Client ID
2) Use this documentation (https://soedemo.stackenterprise.co/api/docs/authentication) to create an access token 
	a. The URL you will need to create will look like the following; 
	https://soedemo.stackenterprise.co/oauth/dialog?client_id=[your_client_id]&scope=write_access,no_expiry&redirect_uri=https://soedemo.stackenterprise.co
	Make sure to replace the URL and client_ID with URLs/client_IDs that are relevant to your organization. 
3) Populate your CSV with questions and answers that you want to seed. Use the format in the attached CSV (seeding.csv)
4) Replace the token in csv_to_api with your access token, then run csv_to_api.py in python3
5) Once csv_to_api.py has POSTed successfully, run answers_post.py 
6) Enjoy the seeded questions in your instance! 

Use the following steps to post Q&A for Stack Overflow for Teams **Business**: 

1) Go to the Admin Settings in your instance of Stack Overflow for Business. Click on **Personal access tokens** in the "API" section of the left-hand menu. Click **Create a new PAT** to create a token. Enable write access, then create the token. For more detail on how to do this - please refer to the following - https://stackoverflowteams.help/en/articles/4385859-stack-overflow-for-teams-api
2) Remove 'key' and 'X-API-Key' from the script. Replace the value for 'token' with your PAT token
3) Populate your CSV with questions and answers that you want to seed. Use the format in the attached CSV (seeding.csv)
4) Replace the token in csv_to_api with your access token, then run csv_to_api.py in python3
5) Once csv_to_api.py has POSTed successfully, run answers_post.py 
6) Enjoy the seeded questions in your instance! 
