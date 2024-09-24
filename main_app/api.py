import requests
import os
from dotenv import load_dotenv
from django.http import JsonResponse


def get_workouts(muscle_group):
  url = "https://work-out-api1.p.rapidapi.com/search"
  querystring = {"Muscles":muscle_group}
  load_dotenv()
  headers = {
    "x-rapidapi-key": os.getenv('API_KEY'),
    "x-rapidapi-host": "work-out-api1.p.rapidapi.com"
  }
  response = requests.get(url, headers=headers, params=querystring)
  
  return response

