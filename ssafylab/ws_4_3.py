import requests
from pprint import pprint as print

dummy_data = []
for juso in range(1,11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{juso}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    
    name = parsed_data['name']
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])
    company_name = parsed_data['company']['name']

    dict_list = {'comepany' : company_name, 'lat' : lat, 'lng' : lng, 'name' : name}
    if 80 > lat > (-80):
         if 80 > lng > (-80):
            dummy_data.append(dict_list)

print(dummy_data)