import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('GIPHY_API_KEY')
endpoint = 'https://api.giphy.com/v1/gifs/trending'
params = {"api_key": API_KEY, "limit": 3, "rating": "g"}

response = requests.get(endpoint, params=params).json()

for gif in response["data"]:
    title = gif["title"]
    trending_date = gif["trending_datetime"]
    url = gif["url"]
    print(f"{title} | Date: {trending_date} | URL: {url}")
