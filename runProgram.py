from PlayerInfo import PlayerInfo
from MatchHistory import MatchHistory
from ChampionInfo import ChampionInfo
from GameInfo import GameInfo

def main():

    gameInfo = GameInfo()
    gameInfo.storeQueueIds()
    gameInfo.storeSeasoninfo()
    gameInfo.storeMapInfo()
    gameInfo.storeGameModeInfo()
    gameInfo.storeGameTypeInfo()


    champions = ChampionInfo()
    champions.storeChampionJson()
    champions.storeChampionPairs("IdKey")
    champions.storeChampionPairs("KeyId")
    print(champions.getChampionKeyOrId("IdKey", "Anivia"))


    summonerName = 'alienburgerpoo'
    summoner = PlayerInfo(summonerName, "na1")
    summoner.storePlayerInfo()


    summonerMatchHistory = MatchHistory(summonerName, "na1")
    summonerMatchHistory.storeMatchHistory()



if __name__ == "__main__":
    main()
