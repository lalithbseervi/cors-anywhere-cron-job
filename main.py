import requests
from bs4 import BeautifulSoup

url = "https://cors-anywhere.herokuapp.com/corsdemo"
session = requests.Session()

response = session.get(url)

print(f"initial fetch status code: {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')

hidden_input = soup.find('input', {'name': 'accessRequest'})

if hidden_input is None:
    print("Hidden input field not found")
    exit()

hidden_value = hidden_input.get('value')
print(f"Hidden input value: {hidden_value}")

form_data = {
    'accessRequest': hidden_value,
}

post_url = url
get_response = session.get(post_url, params=form_data, data=form_data)

if get_response.status_code == 200 or get_response.status_code == 302:
    print("Form submitted successfully")
else:
    print("Form submission failed")

print(get_response.text)