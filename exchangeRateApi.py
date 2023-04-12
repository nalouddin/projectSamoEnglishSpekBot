import requests
from pprint import pprint as print

API_KEY = '099c1e32df0024f04448020e'
currency = 'USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/USD"

# latest

respons = requests.get(url)
# print(respons.status_code)
# print(respons.text)
# print(respons.json())
print(respons.json()['conversion_rate'])