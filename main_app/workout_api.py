import requests
import os
from dotenv import load_dotenv

url = "https://work-out-api1.p.rapidapi.com/search"

querystring = {"Muscles":"biceps"}

load_dotenv()
headers = {
  "x-rapidapi-key": os.getenv('API_KEY'),
	"x-rapidapi-host": "work-out-api1.p.rapidapi.com"
 }

response = requests.get(url, headers=headers, params=querystring)

print(response.json())