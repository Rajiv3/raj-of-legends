import requests
import json
import os
import matplotlib.pyplot as plt
import datetime

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
        self.todayDate = datetime.datetime.today().strftime('%Y%m%d%H%M')
        
        self.serverSettings = ServerSettings(self.server)
        self.championInfo = ChampionInfo(self.server)
        self.fileStorage = FileStorage()
        self.playerInfo = PlayerInfo(self.summonerName, self.server)
        self.gameInfo = GameInfo(self.server)

        # file handling
        self.queueFile = self.queue.title()
        self.championFile = self.champion.replace(" ", "") #no spaces
        self.matchHistoryFile = f"{self.fileStorage.dataStoragePath}/{self.server}/{self.summonerName}/{self.championFile}{self.queueFile}{self.todayDate}MatchHistory.json"
        self.masterMatchHistoryFile = f"{self.fileStorage.dataStoragePath}/{self.server}/{self.summonerName}/MasterMatchHistory.json"
        self.detailedMatchesFolder = f"{self.fileStorage.dataStoragePath}/{self.server}/{self.summonerName}/matches"
        self.gameIdFile = f"{self.fileStorage.dataStoragePath}/{self.server}/{self.summonerName}/GameIds.json"
        
    def inputMatchRange(self):
        """get range of games for match history """
        beginIndex = input("Begin Index: ")
        endIndex = input("End Index: ")
        return beginIndex, endIndex

    def translateChampKey(self, order, champion):
        """helper function to get the champs key in proper format for getMatchHistory"""
        if self.champion != "":
            champKey = self.championInfo.getChampionKeyOrId(order, self.champion)
        else: 
            champKey = ""
        return champKey

    def getMatchHistory(self, range):
        """get the match history with an API call"""
        beginIndex = range[0]
        endIndex = range[1]
        champKey = self.translateChampKey("IdKey", self.champion)
        queueId = self.gameInfo.relevantQueueIds(self.queue)
        accountId = self.playerInfo.getAccountId()

        url = f"{self.serverSettings.api_prefix}{self.serverSettings.apiMatchlistAccountId}{accountId}?champion={champKey}&queue={queueId}&beginIndex={beginIndex}&endIndex={endIndex}&{self.serverSettings.api_suffix}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")

        matchHistory = r.json()['matches']

        return matchHistory

    def storeMatchHistory(self):
        """store the match history in a file"""
        self.fileStorage.makePath(f"{self.fileStorage.dataStoragePath}/{self.server}/{self.summonerName}")
        filename = self.matchHistoryFile

        matchRange = self.inputMatchRange()
        matchHistory = self.getMatchHistory(matchRange)

        with open(filename, 'w') as f:
            json.dump(matchHistory, f, indent=4)

    def storeMasterMatchHistory(self):
        """add the pulled match histories into a master file if they are not already in it """
        self.fileStorage.makePath(f"{self.fileStorage.dataStoragePath}/{self.server}/{self.summonerName}")
        masterFilename = self.masterMatchHistoryFile
        masterMatchHistoryExists = os.path.exists(masterFilename)

        with open(self.matchHistoryFile) as f:
            currentMatchHistory = json.load(f)

        if masterMatchHistoryExists:
            with open(masterFilename) as f:
                masterMatchHistory = json.load(f)
            newMasterMatchHistory = {**currentMatchHistory, **masterMatchHistory}
        else:
            newMasterMatchHistory = currentMatchHistory

        with open(masterFilename, 'w') as f:
            json.dump(newMasterMatchHistory, f, indent=4)

    def getChampionsPlayed(self):
        """return a list of the champions played in the requested matchHistory"""
        # check the file, get a list, return it.
        filename = self.matchHistoryFile
        with open(filename) as f:
            matches = json.load(f)
        
        championsPlayed = []
        for match in matches:
            championKey = str(match["champion"])
            championName = self.championInfo.getChampionKeyOrId("KeyId",championKey)
            championsPlayed.append(championName)
        
        return championsPlayed
    
    def countChampionsPlayed(self):
        """get a count of the number of times each champion is played"""
        championsPlayed = self.getChampionsPlayed()
        countChampions = Counter(championsPlayed)

        return countChampions
    
    def getRolesPlayed(self):
        """return a list of the roles played"""
        filename = self.matchHistoryFile
        with open(filename) as f:
            matches = json.load(f)
        
        rolesPlayed = []
        for match in matches:
            role = match["role"]
            lane = match["lane"]
            roleAndLane = f"{role} {lane}"
            rolesPlayed.append(roleAndLane)
        
        return rolesPlayed

    def countRolesPlayed(self):
        """get a count of the number of times each champion is played"""
        rolesPlayed = self.getRolesPlayed()
        countRoles = Counter(rolesPlayed)

        return countRoles
        
    def getGameIds(self):
        """return a list of the game ids"""
        filename = self.matchHistoryFile
        with open(filename) as f:
            matches = json.load(f)
        
        gameIds = []
        for match in matches:
            gameId = match["gameId"]
            gameIds.append(gameId)
        
        return gameIds

    def storeGameIds(self):
        """store a list of the game ids, use these to keep track for master file"""
        filename = self.gameIdFile
        doGameIdsExist = os.path.exists(filename)
        currentGameIds = self.getGameIds()

        if doGameIdsExist:
            with open(filename, 'r') as f:
                masterGameIds = json.load(f)
            with open(filename, 'w') as f:
                fullGameIds = list(set(masterGameIds + currentGameIds))
                json.dump(fullGameIds, f)
        else:
            with open(filename, 'w') as f:
                json.dump(currentGameIds, f)
    
    def getDetailedMatchData(self, gameId):
        """pull the detailed match data from the API and store it """
        url = f"{self.serverSettings.api_prefix}{self.serverSettings.apiMatchByMatchId}{gameId}?{self.serverSettings.api_suffix}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")

        matchData = r.json()

        return matchData

    def storeDetailedMatchData(self):
        """store the detailed match data """
        self.fileStorage.makePath(self.detailedMatchesFolder)
        gameIds = self.getGameIds()

        for gameId in gameIds:
            # loop through each game ID and store the match file
            gameFilename = f"{self.detailedMatchesFolder}/{gameId}.json"

            matchData = self.getDetailedMatchData(gameId)

            with open(gameFilename, "w") as f:
                json.dump(matchData, f, indent=4)

    def plotMatchHistoryChampions(self):
        """Make a plot of the champions played"""
        # ordereddict better? bit slower but looks better
        championsPlayed = self.countChampionsPlayed()
        figureFilename = f"{self.fileStorage.dataStoragePath}/{self.summonerName}/{self.championFile}{self.queueFile}ChampionsMatchHistory.png"

        # pick different style
        plt.style.use('dark_background')
        fig, ax = plt.subplots()
        ax.bar(championsPlayed.keys(), championsPlayed.values())
        ax.tick_params(axis='x', which='major', rotation=90)
        plt.savefig(figureFilename,bbox_inches='tight')

        return ax
    
    def plotMatchHistoryRoles(self):
        """Make a plot of the roles played"""
        rolesPlayed = self.countRolesPlayed()
        figureFilename = f"{self.fileStorage.dataStoragePath}/{self.summonerName}/{self.championFile}{self.queueFile}RolesMatchHistory.png"

        plt.style.use('dark_background')
        fig, ax = plt.subplots()
        ax.bar(rolesPlayed.keys(), rolesPlayed.values())
        ax.tick_params(axis='x', which='major', rotation=90)
        plt.savefig(figureFilename,bbox_inches='tight')

        return ax

    def displayPlots(self):
        """display the plots"""
        plotChampions = self.plotMatchHistoryChampions()
        plotRoles = self.plotMatchHistoryRoles()

        plt.show()

    def deleteMatchHistoryFile(self):
        os.remove(self.matchHistoryFile)
