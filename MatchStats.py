import os
import json
import matplotlib.pyplot as plt

from MatchHistory import MatchHistory
from FileStorage import FileStorage

class MatchStats:
    """Class to go through the games in the match history and get indepth stats from it"""

    def __init__(self, summonerName, server = "na1", champion = "", queue = ""):
        self.summonerName = summonerName
        self.champion = champion
        self.queue = queue
        self.server = server

        self.fileStorage = FileStorage()
        self.matchHistory = MatchHistory(self.summonerName, self.server, self.champion, self.queue)

        # file handling
        self.queueFile = self.queue.title()
        self.championFile = self.champion.replace(" ", "") #no spaces

        self.specificGameIdFile = f"{self.fileStorage.dataStoragePath}/{self.server}/{self.summonerName}/{self.championFile}{self.queueFile}GameIds.json"

        self.detailedMatchesFolder = f"{self.fileStorage.dataStoragePath}/{self.server}/{self.summonerName}/matches"
        # plot files
        self.figureFilename = f"{self.fileStorage.dataStoragePath}/{self.server}/{self.summonerName}"


    def getParticpantId(self, matchData):
        """stats are sorted by participant ID in the match files, will need to get that everytime"""
        try:
            participants = matchData["participantIdentities"]
        except KeyError:
            pass
        for participant in participants:
            if participant['player']['summonerName'] == self.summonerName:
                participantId = participant['participantId']
        
        return participantId

    def getCsValues(self):
        """get the values for the cs per minute the player in the list of game Ids"""

        gameIdFile = self.specificGameIdFile

        # get the game ids
        with open(gameIdFile) as f:
            gameIds = json.load(f)

        csdList = []

        # loop through all the games in gameIds, getting the csd values for the player
        for game in gameIds:
            try:
                with open(f"{self.detailedMatchesFolder}/{game}.json") as matchFile:
                    # get the participant Id
                    matchData = json.load(matchFile)
                    participantId = self.getParticpantId(matchData)

                    # go into the participants list, if its the correct participant then get the values for CSD (or all stats?)

                    participants = matchData["participants"]

                    for participant in participants:     
                        if participant["participantId"] == participantId:
                            try:
                                csd = participant["timeline"]["creepsPerMinDeltas"]["0-10"]
                                csdList.append(csd)
                            except KeyError:
                                pass
            except FileNotFoundError:
                pass
        
        return csdList

    def plotCsValues(self):
        """Make a plot of the differences in CS"""
        csValues = self.getCsValues()
        numGames = len(csValues)
        figureFilename = f"{self.figureFilename}/CsDifferences.png"

        plt.style.use('dark_background')
        fig, ax = plt.subplots()
        ax.plot(range(numGames), csValues)
        plt.xlabel('Game Number')
        plt.ylabel('CS Per Minute at 10')
        plt.title('CS Per Minute by 10 minutes')
        ax.tick_params(axis='x', which='major', rotation=90)
        plt.savefig(figureFilename,bbox_inches='tight')

        return ax

    def displayPlots(self):
        """display the plots"""
        plotCsDifferences = self.plotCsValues()

        plt.show()
