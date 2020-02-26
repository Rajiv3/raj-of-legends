import os
import json

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

    def getCsDifferences(self):
        """get the values for the cs differential for the player in the list of game Ids"""

        # might want to turn this into a function that pulls all the stats for the player, and then call this in other functions?

        gameIdFile = self.specificGameIdFile

        # get the game ids
        with open(gameIdFile) as f:
            gameIds = json.load(f)

        csdList = []

        # loop through all the games in gameIds, getting the csd values for the player
        for game in gameIds:
            with open(f"{self.detailedMatchesFolder}/{game}.json") as matchFile:
                # get the participant Id
                matchData = json.load(matchFile)
                participantId = self.getParticpantId(matchData)

                # go into the participants list, if its the correct participant then get the values for CSD (or all stats?)

                participants = matchData["participants"]

                for participant in participants:     
                    if participant["participantId"] == participantId:
                        csd = participant["timeline"]["creepsPerMinDeltas"]["0-10"]
                        csdList.append(csd)
        
        return csdList
