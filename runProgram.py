from PlayerInfo import PlayerInfo
from MatchHistory import MatchHistory
from ChampionInfo import ChampionInfo
from GameInfo import GameInfo

def main():

    # gameInfo = GameInfo()
    # gameInfo.storeQueueIds()
    # gameInfo.storeSeasoninfo()
    # gameInfo.storeMapInfo()
    # gameInfo.storeGameModeInfo()
    # gameInfo.storeGameTypeInfo()


    # champions = ChampionInfo()
    # champions.storeChampionJson()
    # champions.storeChampionPairs("IdKey")
    # champions.storeChampionPairs("KeyId")
    # print(champions.getChampionKeyOrId("IdKey", "Anivia"))


    summonerName = 'Rajiv'
    # summoner = PlayerInfo(summonerName, "na1")
    # summoner.storePlayerInfo()


    # summonerMatchHistory = MatchHistory(summonerName, "na1", "Dr. Mundo", "solo")
    summonerMatchHistory = MatchHistory(summonerName, "na1", queue="solo")
    summonerMatchHistory.storeMatchHistory()
    # print(summonerMatchHistory.getChampionsPlayed())
    # print(summonerMatchHistory.countChampionsPlayed())
    # summonerMatchHistory.plotMatchHistoryChampions()
    # summonerMatchHistory.displayPlots()
    summonerMatchHistory.storeDetailedMatchData()


if __name__ == "__main__":
    main()
