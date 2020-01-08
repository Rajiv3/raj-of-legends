from PlayerInfo import PlayerInfo
from MatchHistory import MatchHistory
from ChampionInfo import ChampionInfo

def main():

    champions = ChampionInfo()
    champions.storeChampionJson()

    champions.storeChampionIdKey()

    champions.storeChampionKeyId()


    summonerName = 'YoungAspiring'

    summoner = PlayerInfo(summonerName)
    
    summoner.storePlayerInfo()


    summonerMatchHistory = MatchHistory(summonerName)
    summonerMatchHistory.storeMatchHistory()



if __name__ == "__main__":
    main()
