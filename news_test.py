import requests

url = "http://localhost:8080/news"
response = requests.get(url)

print(response.text)