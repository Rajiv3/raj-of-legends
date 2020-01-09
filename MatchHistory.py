import requests
import json
import os
from APIKey import api_key
from PlayerInfo import PlayerInfo
from ServerSettings import ServerSettings
from ChampionInfo import ChampionInfo
from FileStorage import FileStorage

class MatchHistory:
    """Class to get and maintain the match history of a user"""
    # Note that there is a limit to how far back the data can be fetched
    # don't want to delete old data (how to solve? diff files?)

    def __init__(self, summonerName, server = "na1", champion = "", queue = ""):
        self.summonerName = summonerName
        self.champion = champion
        self.queue = queue
        self.server = server
        self.serverSettings = ServerSettings(server)
        self.championInfo = ChampionInfo()
        self.fileStorage = FileStorage()
    
    def checkPlayerData(self):
        """check if data for the user already exists, if not, build it"""
        pass

    def getAccountId(self):
        """pull the required user info from the file"""
        filename = f"{self.fileStorage.dataStoragePath}/{self.summonerName}/{self.summonerName}PlayerSummary.json"
        with open(filename) as f:
            playerData = json.load(f)
        accountId = playerData['Account ID']

        return accountId

    def getMatchHistory(self):
        """get the match history with an API call"""

        # queue from queue name
        if self.champion != "":
            champKey = self.championInfo.championIdToKey(self.champion)
        else: 
            champKey = ""
        
        accountId = self.getAccountId()
        url = f"{self.serverSettings.api_prefix}{self.serverSettings.apiMatchlistAccountId}{accountId}?champion={champKey}&queue={self.queue}&{self.serverSettings.api_suffix}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")

        matchHistory = r.json()

        return matchHistory
    
    def storeMatchHistory(self):
        """store the match history in a file"""
        self.fileStorage.makePath(f"{self.fileStorage.dataStoragePath}/{self.summonerName}")
        filename = f"{self.fileStorage.dataStoragePath}/{self.summonerName}/{self.summonerName}MatchHistory.json"

        matchHistory = self.getMatchHistory()

        with open(filename, 'w') as f:
            json.dump(matchHistory, f, indent=4)
    
    def championsPlayed(self):
        """return a list of the champions played in the provided matchHistory"""
        pass
