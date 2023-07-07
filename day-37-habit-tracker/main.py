import requests
from datetime import datetime

USER_NAME = 'tamil'
TOKEN = 'tmlganjan'
GRAPH_ID = 'graph1'

# POST method
pixela_endpoint = 'https://pixe.la/v1/users'  # https://pixe.la/
user_parameters = {
    'token': TOKEN,
    'username': USER_NAME,  # https://pixe.la/@tamil  # profile created.
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}  # https://docs.pixe.la/
# https://requests.readthedocs.io/en/latest/api/
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs'
graph_config = {
    'id': GRAPH_ID,
    'name': 'Cycling Graph',
    'unit': 'km',
    'type': 'float',
    'color': 'sora',
}

HEADERS = {
    'X-USER-TOKEN': TOKEN
}

response = requests.post(url=graph_endpoint, params=graph_config, headers=HEADERS)
print(response.text)

post_pixel_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}'
today = datetime.now().strftime('%Y%m%d')  # https://www.w3schools.com/python/python_datetime.asp
parameters = {
    'date': today,
    'quantity': input("How many kilometers?"),
}

HEADERS = {
    'X-USER-TOKEN': TOKEN
}

response = requests.post(url=post_pixel_endpoint, params=parameters, headers=HEADERS)
print(response.text)

# PUT method
date = datetime(year=2023, month=7, day=7).strftime('%Y%m%d')
update_pixel_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date}'
parameters = {
    'quantity': input("How many kilometers?")
}

HEADERS = {
    'X-USER-TOKEN': TOKEN
}
response = requests.put(url=update_pixel_endpoint, params=parameters, headers=HEADERS)
print(response.text)

# PUT method
date = datetime(year=2023, month=7, day=6).strftime('%Y%m%d')
delete_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date}"
HEADERS = {
    'X-USER-TOKEN': TOKEN
}

response = requests.delete(url=delete_pixel_endpoint, headers=HEADERS)
print(response.text)
