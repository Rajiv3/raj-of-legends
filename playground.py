from APIKey import api_key
import requests
import json

urlRank = f"https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/UhSQpb_Hl8HWnkPpja0W8qbNlEpB8FNHpHIQJRu4pjoTcAI?api_key={api_key}"
rRank = requests.get(urlRank)
print(f"Status code: {rRank.status_code}")
userRankData = rRank.json()

with open("testing.json", 'w') as f:
    json.dump(userRankData, f, indent=4)
print(userRankData)
