import requests
import json
import os
import matplotlib.pyplot as plt
from collections import Counter
from APIKey import api_key
from PlayerInfo import PlayerInfo
from ServerSettings import ServerSettings
from ChampionInfo import ChampionInfo
from FileStorage import FileStorage
from GameInfo import GameInfo
class MatchHistory:
    """Class to get and maintain the match history of a user"""
    # Note that there is a limit to how far back the data can be fetched
    # don't want to delete old data (how to solve? add to dictionary?)

    def __init__(self, summonerName, server = "na1", champion = "", queue = ""):
        self.summonerName = summonerName
        self.champion = champion
        self.queue = queue
        self.server = server
        self.serverSettings = ServerSettings(self.server)
        self.championInfo = ChampionInfo(self.server)
        self.fileStorage = FileStorage()
        self.playerInfo = PlayerInfo(self.summonerName, self.server)
        self.gameInfo = GameInfo(self.server)

        # file handling
        self.queueFile = self.queue.title() #prettier
        self.championFile = self.champion.replace(" ", "") #no spaces
    
    def checkPlayerData(self):
        """check if data for the user already exists, if not, build it"""
        pass

    def getMatchHistory(self):
        """get the match history with an API call"""
        if self.champion != "":
            champKey = self.championInfo.getChampionKeyOrId("IdKey", self.champion)
        else: 
            champKey = ""
        queueId = self.gameInfo.relevantQueueIds(self.queue)
        accountId = self.playerInfo.getAccountId()

        url = f"{self.serverSettings.api_prefix}{self.serverSettings.apiMatchlistAccountId}{accountId}?champion={champKey}&queue={queueId}&{self.serverSettings.api_suffix}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")

        matchHistory = r.json()

        return matchHistory
    
    def storeMatchHistory(self):
        """store the match history in a file"""
        self.fileStorage.makePath(f"{self.fileStorage.dataStoragePath}/{self.summonerName}")
        filename = f"{self.fileStorage.dataStoragePath}/{self.summonerName}/{self.summonerName}{self.championFile}{self.queueFile}MatchHistory.json"

        matchHistory = self.getMatchHistory()   

        with open(filename, 'w') as f:
            json.dump(matchHistory, f, indent=4)
    
    def getChampionsPlayed(self):
        """return a list of the champions played in the requested matchHistory"""
        # check the file, get a list, return it.
        filename = f"{self.fileStorage.dataStoragePath}/{self.summonerName}/{self.summonerName}{self.championFile}{self.queueFile}MatchHistory.json"
        with open(filename) as f:
            matches = json.load(f)["matches"]
        
        championsPlayed = []
        for match in matches:
            championKey = str(match["champion"])
            championName = self.championInfo.getChampionKeyOrId("KeyId",championKey)
            championsPlayed.append(championName)
        
        return championsPlayed
    
    def countChampionsPlayed(self):
        """get a count of the number of times each champion is played"""
        # use this instead of list form?
        championsPlayed = self.getChampionsPlayed()
        countChampions = Counter(championsPlayed)

        return countChampions
    
    def getRolesPlayed(self):
        """return a list of the roles played"""
        filename = f"{self.fileStorage.dataStoragePath}/{self.summonerName}/{self.summonerName}{self.championFile}{self.queueFile}MatchHistory.json"
        with open(filename) as f:
            matches = json.load(f)["matches"]
        
        rolesPlayed = []
        for match in matches:
            role = match["role"]
            lane = match["lane"]
            roleAndLane = f"{role} {lane}"
            rolesPlayed.append(roleAndLane)
        
        return rolesPlayed
        
    def getGameIds(self):
        """return a list of the game ids"""
        filename = f"{self.fileStorage.dataStoragePath}/{self.summonerName}/{self.summonerName}{self.championFile}{self.queueFile}MatchHistory.json"
        with open(filename) as f:
            matches = json.load(f)["matches"]
        
        gameIds = []
        for match in matches:
            gameId = match["gameId"]
            gameIds.append(gameId)
        
        return gameIds

    def plotMatchHistoryChampions(self):
        """Make a plot of the champions played"""
        championsPlayed = self.countChampionsPlayed()
        figureFilename = f"{self.fileStorage.dataStoragePath}/{self.summonerName}/{self.summonerName}{self.championFile}{self.queueFile}MatchHistory.png"

        plt.style.use('dark_background')
        fig, ax = plt.subplots()
        ax.bar(championsPlayed.keys(), championsPlayed.values())
        ax.tick_params(axis='x', which='major', rotation=90)
        plt.savefig(figureFilename,bbox_inches='tight')

        return ax
    
    def displayPlots(self):
        """display the plots"""
        matchHistoryChampions = self.plotMatchHistoryChampions()

        plt.show()
