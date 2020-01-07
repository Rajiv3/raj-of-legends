import requests
from APIKey import api_key
import json
import os

class UserInfo:
    """class to get user info"""

    def __init__(self, summonerName, server = "na1"):
        """initialize class """
        self.summonerName = summonerName
        self.server = server
        self.api_prefix = f"https://{self.server}.api.riotgames.com"

    # combined into one longer funciton to minimize API calls
    def getUserInfo(self):
        """get the user info from API"""
        url = f"{self.api_prefix}/lol/summoner/v4/summoners/by-name/{self.summonerName}?api_key={api_key}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")
        userData = r.json()

        playerInfo = {}
        playerInfo["Summoner name"] = userData['name']
        playerInfo["Summoner ID"] = userData['id']
        playerInfo["Account ID"] = userData['accountId']
        playerInfo["Level"] = userData['summonerLevel']
        playerInfo["Profile Pic"] = userData['profileIconId']

        urlRank = f"{self.api_prefix}/lol/league/v4/entries/by-summoner/{playerInfo['Summoner ID']}?api_key={api_key}"
        rRank = requests.get(urlRank)
        print(f"Status code: {r.status_code}")
        userRankData = rRank.json()
        
        playerRankInfo = {}
        playerRankInfo["Queue Type"] = userRankData[0]['queueType']
        playerRankInfo["Tier"] = userRankData[0]['tier']
        playerRankInfo["Rank"] = userRankData[0]['rank']
        playerRankInfo["Wins"] = userRankData[0]['wins']
        playerRankInfo["Losses"] = userRankData[0]['losses']
        
        fullPlayerInfo = {**playerInfo, **playerRankInfo}

        return fullPlayerInfo

    def storeUserInfo(self):
        """function to store the information about the summoner"""
        if not os.path.exists(f"data/{self.summonerName}"):
            os.makedirs(f"data/{self.summonerName}")
        filename = f"data/{self.summonerName}/{self.summonerName}PlayerSummary.json"

        playerInfo = self.getUserInfo()

        with open(filename, 'w') as f:
            json.dump(playerInfo, f, indent=4)

def main():
    summonerRajiv = UserInfo("Rajiv")

    userInfo = summonerRajiv.getUserInfo()

    for k,v in userInfo.items():
        print(f"{k}: {v}")
    
    summonerRajiv.storeUserInfo()

if __name__ == "__main__":
    main()
