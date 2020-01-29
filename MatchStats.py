import os
import json

import MatchHistory
import FileStorage

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


    def getParticpantId(self):
        """stats are sorted by participant ID in the match files, will need to get that everytime"""
        pass

    def getCsDifferences(self):
        """get the values for the cs differential for the player in the list of game Ids"""
        # this will be a list of tuples?
        gameIdFile = self.specificGameIdFile

        # get the game ids
        with open(gameIdFile) as f:
            gameIds = json.load(f)

        # loop through all the games in gameIds, getting the 3 values for csd for the player
        for game in gameIds:
            with open(f"gameFilename{matchId}.json") as f:
                # get the participant Id
                participantId = self.getParticpantId()

                # go into the participants list, if its the correct participant then get the values for CSD
                if value == participantId:
                    pass
