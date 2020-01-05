import requests
from APIKey import api_key

def getUserJson():
    url = "https://na1.api.riotgames.com//lol/summoner/v4/summoners/by-name/Rajiv?api_key=" + api_key 
    r = requests.get(url)
    print(f"Status code: {r.status_code}:")

    article_ids = r.json()
    return article_ids

article_ids = getUserJson()

print(article_ids)
