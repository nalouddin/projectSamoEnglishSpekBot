import requests
import json

app_id = "<your_app_id>"
app_key = "<your_app_key>"

language = "en-gb"

word_id = "example"

url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

r = requests.get(url, headers={"app_id": <your_app_id>, "app_key": <your_app_key>})