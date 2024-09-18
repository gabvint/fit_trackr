import requests
import os
from dotenv import load_dotenv
import json


def get_workouts(muscle_group):
  url = "https://work-out-api1.p.rapidapi.com/search"
  querystring = {"Muscles":muscle_group}
  load_dotenv()
  headers = {
    "x-rapidapi-key": os.getenv('API_KEY'),
    "x-rapidapi-host": "work-out-api1.p.rapidapi.com"
  }
  response = requests.get(url, headers=headers, params=querystring)
  
  return response.json()



# if response.status_code == 200:
#     data = response.json()
    
#     muscles = [item['WorkOut'] for item in data if 'Muscles' in item]
    
#     print(muscles)
# else:
#     print(f"Error: {response.status_code}")
  
#print(response.json())

