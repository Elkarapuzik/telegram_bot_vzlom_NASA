import os
import requests
from pprint import pprint
#______________________________
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

params = {
    "count" : "10",
    "api_key" : api_key,
}

response = requests.get(f'https://api.nasa.gov/planetary/apod', params=params )
response.raise_for_status()

name = 0

for slovar in response.json():
    response = requests.get(slovar['url'])
    response.raise_for_status()
    name = name + 1
    number_of_name = f"picture{name}.jpeg"
    with open(number_of_name, "wb") as file:
        file.write(response.content)