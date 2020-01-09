import os
import json
import requests
from FileStorage import FileStorage
from ServerSettings import ServerSettings

class GameInfo:
    """class to get information about the game from API"""

    def __init__(self, server = "na1"):
        self.fileStorage = FileStorage()
        self.serverSettings = ServerSettings(server)

    def getQueueIds(self):
        """get the information about the queues"""
        url = f"{self.serverSettings.staticQueueIdsUrl}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")
        QueueIds = r.json()
        
        return QueueIds

    def storeQueueIds(self):
        """Store the information about the queues """
        self.fileStorage.makePath(f"{self.fileStorage.staticDataStoragePath}")
        filename = f"{self.fileStorage.staticDataStoragePath}/QueueIds.json"

        queueIds = self.getQueueIds()

        with open(filename, 'w') as f:
            json.dump(queueIds, f, indent=4)

    def getSeasonInfo(self):
        """get the information about the seasons"""
        url = f"{self.serverSettings.staticSeasonsUrl}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")
        seasons = r.json()
        
        return seasons

    def storeSeasoninfo(self):
        """store the information about the season info"""
        self.fileStorage.makePath(f"{self.fileStorage.staticDataStoragePath}")
        filename = f"{self.fileStorage.staticDataStoragePath}/SeasonInfo.json"

        seasonInfo = self.getSeasonInfo()

        with open(filename, 'w') as f:
            json.dump(seasonInfo, f, indent=4)

    def getMapInfo(self):
        """get the information about the maps"""
        url = f"{self.serverSettings.staticMapsUrl}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")
        mapInfo = r.json()
        
        return mapInfo

    def storeMapInfo(self):
        """store the information about the maps"""
        self.fileStorage.makePath(f"{self.fileStorage.staticDataStoragePath}")
        filename = f"{self.fileStorage.staticDataStoragePath}/MapInfo.json"

        mapInfo = self.getMapInfo()

        with open(filename, 'w') as f:
            json.dump(mapInfo, f, indent=4)

    def getGameModeInfo(self):
        """get the information about the Game Types"""
        url = f"{self.serverSettings.staticGameModesUrl}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")
        gameModeInfo = r.json()
        
        return gameModeInfo

    def storeGameModeInfo(self):
        """store the information about the Game Typess"""
        self.fileStorage.makePath(f"{self.fileStorage.staticDataStoragePath}")
        filename = f"{self.fileStorage.staticDataStoragePath}/GameModeInfo.json"

        gameModeInfo = self.getGameModeInfo()

        with open(filename, 'w') as f:
            json.dump(gameModeInfo, f, indent=4)

    def getGameTypeInfo(self):
        """get the information about the Game Types"""
        url = f"{self.serverSettings.staticGameTypesUrl}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")
        gameTypeInfo = r.json()
        
        return gameTypeInfo

    def storeGameTypeInfo(self):
        """store the information about the Game Types"""
        self.fileStorage.makePath(f"{self.fileStorage.staticDataStoragePath}")
        filename = f"{self.fileStorage.staticDataStoragePath}/GameTypeInfo.json"

        gameTypeInfo = self.getGameTypeInfo()

        with open(filename, 'w') as f:
            json.dump(gameTypeInfo, f, indent=4)
