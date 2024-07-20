import requests
from requests_ntlm import HttpNtlmAuth
import json

username = "usuario"
password = "pass"
auth = HttpNtlmAuth(username,password)

api_url = f"http://laurl"
response = requests.get(url=api_url, auth=auth)

print(f"Output: {response.content}")