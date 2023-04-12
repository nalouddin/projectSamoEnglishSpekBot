import requests
from pprint import pprint as print

sura = 1
oyat = 4
tafsir = 'uzb-alaaudeenmansou'

url_oyat = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json'
url_sura = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json'

request = requests.get(url_oyat)
res = request.json()
print(res.keys())