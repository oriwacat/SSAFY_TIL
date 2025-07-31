import requests
from pprint import pprint as print

dummy_data = []
for juso in range(1,11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{juso}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])

print(dummy_data)