import json
import requests
import os
from ServerSettings import ServerSettings

class ChampionInfo:
    """class to get information about champions"""

    def __init__(self):
        self.serverSettings = ServerSettings()
        self.championJsonFilename = f"data/championInfo.json"
        self.championKeyIdFilename = f"data/ChampionKeyIdPairs.json"
        self.championIdKeyFilename = f"data/ChampionIdKeyPairs.json"

    def checkChampionJson(self):
        """check if the champion info json exists"""
        # if it does not, run storeChampionJson.
        pass

    def getChampionJson(self):
        url = f"{self.serverSettings.dragonChampJson}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")

        champions = r.json()

        return champions

    def storeChampionJson(self):
        """save the entire champion json"""
        if not os.path.exists(f"{self.championJsonFilename}"):
            os.makedirs(f"{self.championJsonFilename}")

        champions = self.getChampionJson()

        filename = f"{self.championJsonFilename}"
        with open(filename, 'w') as f:
            json.dump(champions, f, indent=4)

        
    def matchChampionKeyId(self):
        """match the champion key with the name of the champion,return dict"""

        filename = f"{self.championJsonFilename}"
        with open(filename) as f:
            fullChampionInfo = json.load(f)

        allChampions = fullChampionInfo['data']

        championIds = []
        championKeyIds = {}
        for champion in allChampions:
            championIds.append(champion)
        
        for championName in championIds:
            key = allChampions[championName]['key']
            champion = allChampions[championName]['name']
            championKeyIds[key] = champion
        
        return championKeyIds
    
    def storeChampionKeyId(self):
        """store the champion Key ID pairs in a file"""
        if not os.path.exists(f"data"):
            os.makedirs(f"data")
        filename = f"{self.championKeyIdFilename}"

        championsKeyId = self.matchChampionKeyId()

        with open(filename, 'w') as f:
            json.dump(championsKeyId, f, indent=4)

    def matchChampionIdKey(self):
        """match the champion name with the key of the champion,return dict"""

        filename = f"{self.championJsonFilename}"
        with open(filename) as f:
            fullChampionInfo = json.load(f)

        allChampions = fullChampionInfo['data']

        championIds = []
        championIdKeys = {}
        for champion in allChampions:
            championIds.append(champion)
        
        for championName in championIds:
            champion = allChampions[championName]['name']
            key = allChampions[championName]['key']
            championIdKeys[champion] = key
        
        return championIdKeys
    
    def storeChampionIdKey(self):
        """store the champion IDs in a file"""
        if not os.path.exists(f"data"):
            os.makedirs(f"data")
        filename = f"{self.championIdKeyFilename}"

        championsIdKey = self.matchChampionIdKey()

        with open(filename, 'w') as f:
            json.dump(championsIdKey, f, indent=4)

        return filename

    def championIdToKey(self, championId):
        """Enter champion ID(name), return key"""
        filename = f"{self.championIdKeyFilename}"
        with open(filename) as f:
            championIdKeyPairs = json.load(f)
        
        championKey = championIdKeyPairs[championId]
        return championKey

    def championKeyToId(self, championId):
        """Enter champion key, return ID(name)"""
        filename = f"{self.championKeyIdFilename}"
        with open(filename) as f:
            championKeyIdPairs = json.load(f)

        championId = championIdKeyPairs[championId]
        return championId
