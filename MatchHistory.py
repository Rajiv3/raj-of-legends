import requests
import json
import os
from APIKey import api_key
from PlayerInfo import PlayerInfo
from ServerSettings import ServerSettings


class MatchHistory:
    """Class to get and maintain the match history of a user"""
    # Note that there is a limit to how far back the data can be fetched
    # don't want to delete old data (how to solve? diff files?)

    # before running match history, must have the accountId of the summoner
    # can get it from the file - check existence of file (if it doesnt?)

    def __init__(self, summonerName):
        self.summonerName = summonerName
        self.serverSettings = ServerSettings("na1")
    
    def checkPlayerData(self):
        """check if data for the user already exists, if not, build it"""
        pass

    def getAccountId(self):
        """pull the required user info from the file"""
        # ToDo: check file exists
        filename = f"data/{self.summonerName}/{self.summonerName}PlayerSummary.json"
        with open(filename) as f:
            playerData = json.load(f)
        accountId = playerData['Account ID']

        return accountId 

    def getMatchHistory(self):
        """get the match history with an API call"""
        accountId = self.getAccountId()
        url = f"{self.serverSettings.api_prefix}/lol/match/v4/matchlists/by-account/{accountId}{self.serverSettings.api_suffix}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")

        matchHistory = r.json()

        return matchHistory
    
    def storeMatchHistory(self):
        """store the match history in a file"""
        if not os.path.exists(f"data/{self.summonerName}"):
            os.makedirs(f"data/{self.summonerName}")
        filename = f"data/{self.summonerName}/{self.summonerName}MatchHistory.json"

        matchHistory = self.getMatchHistory()

        with open(filename, 'w') as f:
            json.dump(matchHistory, f, indent=4)
