import requests
import json
import os

from APIKey import api_key
from ServerSettings import ServerSettings
from FileStorage import FileStorage

class PlayerInfo:
    """class to get user info"""

    def __init__(self, summonerName, server = "na1"):
        """initialize class """
        self.server = server
        self.summonerName = summonerName
        self.serverSettings = ServerSettings(self.server)
        self.fileStorage = FileStorage()
        self.playerSummaryFilename = f"{self.fileStorage.dataStoragePath}/{self.summonerName}/{self.summonerName}PlayerSummary.json"


    # combined into one longer function to minimize API calls
    # this is not called all the time to reduce calls to the API
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
        self.fileStorage.makePath(f"{self.fileStorage.dataStoragePath}/{self.summonerName}")

        playerInfo = self.getPlayerInfo()

        with open(self.playerSummaryFilename, 'w') as f:
            json.dump(playerInfo, f, indent=4)

    # below are the methods to call the player info. These are used instead of
    # getPlayerInfo() because that calls the api each time
    # putting them in seperate methods makes it easier to use in other places
    def getSummonerName(self):
        """pull the required user info from the file"""
        with open(self.playerSummaryFilename) as f:
            playerData = json.load(f)
        summonerName = playerData['Summoner name']

        return summonerName

    def getSummonerID(self):
        """pull the required user info from the file"""
        with open(self.playerSummaryFilename) as f:
            playerData = json.load(f)
        summonerId = playerData['Summoner ID']

        return summonerId

    def getAccountId(self):
        """pull the required user info from the file"""
        with open(self.playerSummaryFilename) as f:
            playerData = json.load(f)
        accountId = playerData['Account ID']

        return accountId
        
    def getPlayerLevel(self):
        """pull the required user info from the file"""
        with open(self.playerSummaryFilename) as f:
            playerData = json.load(f)
        playerLevel = playerData['Level']

        return playerLevel

    def getProfilePic(self):
        """pull the required user info from the file"""
        with open(self.playerSummaryFilename) as f:
            playerData = json.load(f)
        profilePic = playerData['Profile Pic']

        return profilePic
        
    def getQueueType(self):
        """pull the required user info from the file"""
        with open(self.playerSummaryFilename) as f:
            playerData = json.load(f)
        queueType = playerData['Queue Type']

        return queueType

    def getPlayerTier(self):
        """pull the required user info from the file"""
        with open(self.playerSummaryFilename) as f:
            playerData = json.load(f)
        playerTier = playerData['Tier']

        return playerTier

    def getPlayerRank(self):
        """pull the required user info from the file"""
        with open(self.playerSummaryFilename) as f:
            playerData = json.load(f)
        playerRank = playerData['Rank']

        return playerRank

    def getPlayerWins(self):
        """pull the required user info from the file"""
        with open(self.playerSummaryFilename) as f:
            playerData = json.load(f)
        playerWins = playerData['Wins']

        return playerWins
        
    def getPlayerLosses(self):
        """pull the required user info from the file"""
        with open(self.playerSummaryFilename) as f:
            playerData = json.load(f)
        playerLosses = playerData['Losses']

        return playerLosses
