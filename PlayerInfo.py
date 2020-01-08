import requests
import json
import os

from APIKey import api_key
from ServerSettings import ServerSettings


class PlayerInfo:
    """class to get user info"""

    def __init__(self, summonerName, server = "na1"):
        """initialize class """
        self.summonerName = summonerName
        self.serverSettings = ServerSettings('na1')

    # combined into one longer funciton to minimize API calls
    def getPlayerInfo(self):
        """get the user info from API"""
        url = f"{self.serverSettings.api_prefix}{self.serverSettings.apiPlayerSummonerName}{self.summonerName}?{self.serverSettings.api_suffix}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")
        userData = r.json()

        playerInfo = {}
        playerInfo["Summoner name"] = userData['name']
        playerInfo["Summoner ID"] = userData['id']
        playerInfo["Account ID"] = userData['accountId']
        playerInfo["Level"] = userData['summonerLevel']
        playerInfo["Profile Pic"] = userData['profileIconId']

        urlRank = f"{self.serverSettings.api_prefix}{self.serverSettings.apiRankedStatsSummonerName}{playerInfo['Summoner ID']}?{self.serverSettings.api_suffix}"
        rRank = requests.get(urlRank)
        print(f"Status code: {rRank.status_code}")
        userRankData = rRank.json()
        
        playerRankInfo = {}
        for queueData in userRankData:
            if queueData['queueType'] == "RANKED_SOLO_5x5":
                playerRankInfo["Queue Type"] = queueData['queueType']
                playerRankInfo["Tier"] = queueData['tier']
                playerRankInfo["Rank"] = queueData['rank']
                playerRankInfo["Wins"] = queueData['wins']
                playerRankInfo["Losses"] = queueData['losses']
            else:
                continue
        
        fullPlayerInfo = {**playerInfo, **playerRankInfo}

        return fullPlayerInfo

    def storePlayerInfo(self):
        """function to store the information about the summoner"""
        if not os.path.exists(f"data/{self.summonerName}"):
            os.makedirs(f"data/{self.summonerName}")
        filename = f"data/{self.summonerName}/{self.summonerName}PlayerSummary.json"

        playerInfo = self.getPlayerInfo()

        with open(filename, 'w') as f:
            json.dump(playerInfo, f, indent=4)
