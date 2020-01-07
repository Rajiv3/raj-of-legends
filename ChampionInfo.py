import json
import requests
import os

class ChampionInfo:
    """class to get information about champions"""

    def __init__(self):
        self.championJsonFilename = 'data/championInfo.json'

    def checkChampionJson(self):
        """check if the champion info json exists"""
        pass

    def getChampionJson(self):
        """get the entire champion json"""
        url = f"https://ddragon.leagueoflegends.com/cdn/9.24.2/data/en_US/champion.json"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")

        champions = r.json()

        filename = f"{self.championJsonFilename}"
        with open(filename, 'w') as f:
            json.dump(champions, f, indent=4)
        
    def matchChampionIds(self):
        """match the champion ID with the name of the champion"""

        filename = f"{self.championJsonFilename}"
        with open(filename) as f:
            fullChampionInfo = json.load(f)

        allChampions = fullChampionInfo['data']

        championNames = []
        championIds = {}
        for champion in allChampions:
            championNames.append(champion)
        
        for championName in championNames:
            key = allChampions[championName]['key']
            champion = allChampions[championName]['name']
            championIds[key] = champion
        
        return championIds
    
    def storeChampionIds(self):
        """store the champion IDs in a file"""
        if not os.path.exists(f"data"):
            os.makedirs(f"data")
        filename = f"data/ChampionKeyIdPairs.json"

        championsIds = self.matchChampionIds()

        with open(filename, 'w') as f:
            json.dump(championsIds, f, indent=4)
