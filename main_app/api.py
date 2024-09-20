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


# def get_foods(food_search):
#   api_key = os.getenv('FOOD_API_KEY')
#   url = "https://api.nal.usda.gov/fdc/v1/foods/search"
#   params = {
#         "query": food_search,
#         "pageSize": 10,
#         "api_key": api_key
#     }
#   response = requests.get(url, params=params)
#   print(f"Request URL: {response.url}")

#   return response