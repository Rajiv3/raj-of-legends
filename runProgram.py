from PlayerInfo import PlayerInfo
from MatchHistory import MatchHistory
from ChampionInfo import ChampionInfo

def main():
    # summonerName = input("Please enter a summoner name: ")
    summonerName = 'Rajiv'

    summoner = PlayerInfo(summonerName)

    # userInfo = summoner.getPlayerInfo()

    # for k,v in userInfo.items():
    #     print(f"{k}: {v}")
    
    summoner.storePlayerInfo()

    summonerMatchHistory = MatchHistory(summonerName)
    summonerMatchHistory.storeMatchHistory()

    champions = ChampionInfo()
    champions.getChampionJson()
    champions.matchChampionIds()
    champions.storeChampionIds()

if __name__ == "__main__":
    main()
