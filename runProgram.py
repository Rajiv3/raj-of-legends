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
    champions.storeChampionKeyId("IdKey")
    champions.storeChampionKeyId("KeyId")
    print(champions.getChampionKeyOrId("IdKey", "Anivia"))


    summonerName = 'Rajiv'
    summoner = PlayerInfo(summonerName, "na1")
    summoner.storePlayerInfo()


    summonerMatchHistory = MatchHistory(summonerName, "na1")
    summonerMatchHistory.storeMatchHistory()



if __name__ == "__main__":
    main()
