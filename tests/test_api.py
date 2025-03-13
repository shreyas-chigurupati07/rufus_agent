import requests

API_URL = "http://127.0.0.1:8000/scrape/"

data = {
    "url": "https://mitadmissions.org/help/faq/",
    "max_depth": 1
}

response = requests.post(API_URL, json=data)
print(response.json())