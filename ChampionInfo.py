import json
import requests
import os
from ServerSettings import ServerSettings
from FileStorage import FileStorage

class ChampionInfo:
    """class to get information about champions"""

    def __init__(self, server = "na1"):
        self.serverSettings = ServerSettings(server)
        self.fileStorage = FileStorage()
        self.championInfoDirectory = f"Champions"
        self.championJsonFilename = f"{self.fileStorage.dataStoragePath}/{self.championInfoDirectory}/championInfo.json"
        self.championKeyIdFilename = f"{self.fileStorage.dataStoragePath}/{self.championInfoDirectory}/championKeyIdPairs.json"
        self.championIdKeyFilename = f"{self.fileStorage.dataStoragePath}/{self.championInfoDirectory}/championIdKeyPairs.json"
        

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
        self.fileStorage.makePath(f"{self.fileStorage.dataStoragePath}/{self.championInfoDirectory}")

        champions = self.getChampionJson()

        filename = f"{self.championJsonFilename}"
        with open(filename, 'w') as f:
            json.dump(champions, f, indent=4)

    def buildChampionPairs(self, order):
        """match the champion key with the name of the champion,return dict"""
        filename = f"{self.championJsonFilename}"
        with open(filename) as f:
            fullChampionInfo = json.load(f)

        allChampions = fullChampionInfo['data']

        championIds = []
        championPairs = {}
        
        for champion in allChampions:
            championIds.append(champion)
        
        for championName in championIds:
            key = allChampions[championName]['key']
            champion = allChampions[championName]['name']
            if order == "KeyId":
                championPairs[key] = champion
            elif order == "IdKey":
                championPairs[champion] = key
        return championPairs

    def storeChampionPairs(self, order):
        """helper function to store the champion key/id pairs"""
        self.fileStorage.makePath(f"{self.fileStorage.dataStoragePath}/{self.championInfoDirectory}")
        if order == "KeyId":
            filename = f"{self.championKeyIdFilename}"
        elif order == "IdKey":
            filename = f"{self.championIdKeyFilename}"

        championsPair = self.buildChampionPairs(order)

        with open(filename, 'w') as f:
            json.dump(championsPair, f, indent=4)

    def getChampionKeyOrId(self, order, champion):
        """helper function to return the champ if either Id or Key is entered"""
        if order == "KeyId":
            filename = f"{self.championKeyIdFilename}"
        elif order == "IdKey":
            filename = f"{self.championIdKeyFilename}"

        with open(filename) as f:
            championPairs = json.load(f)
        
        champion = championPairs[champion]
        return champion
