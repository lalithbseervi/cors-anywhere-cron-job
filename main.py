import requests
import os
from urllib.parse import urlencode

username = os.getenv('USERNAME', 'PES1UG22CA000')  
password = os.getenv('PASSWORD', 'thisisapassword')  

base_url = 'https://cors-proxy.devpages.workers.dev/'
target_url = 'https://pesu-auth-z18n.onrender.com/authenticate'
url = f"{base_url}?url={requests.utils.quote(target_url, safe='')}"

payload = {
    'username': username,
    'password': password,
    'profile': True,
    'fields': ['branch', 'semester', 'name']
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200 or response.status_code == 302:
    print("Form submitted successfully")
else:
    print("Form submission failed")

print(response.text)