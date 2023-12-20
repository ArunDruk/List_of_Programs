import requests
from requests.auth import HTTPBasicAuth
# Making a get request
response = requests.get('https://api.github.com')

# printing request text
print(response.text)
print(response.content)