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

    def getUserInfo(self):
        """get the user info from API"""
        url = f"{self.api_prefix}/lol/summoner/v4/summoners/by-name/{self.summonerName}?api_key={api_key}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")
        userInfo = r.json()

        summonerInfo = {}
        summonerInfo["Summoner name"] = userInfo['name']
        summonerInfo["Summoner ID"] = userInfo['id']
        summonerInfo["Account ID"] = userInfo['accountId']
        summonerInfo["Level"] = userInfo['summonerLevel']
        summonerInfo["Profile Pic"] = userInfo['profileIconId']
        return summonerInfo

    # current issue: This calls the API twice. 
    # Would prefer to write to something then call from there rather than 
    # calling the API multiple times?        
    def getUserRankInfo(self):
        """get the users rank info from API"""
        summonerId = self.getUserInfo()["Summoner ID"]
        url = f"{self.api_prefix}/lol/league/v4/entries/by-summoner/{summonerId}?api_key={api_key}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")
        userRankData = r.json()

        summonerRankInfo = {}
        summonerRankInfo["Queue Type"] = userRankData[0]['queueType']
        summonerRankInfo["Tier"] = userRankData[0]['tier']
        summonerRankInfo["Rank"] = userRankData[0]['rank']
        summonerRankInfo["Wins"] = userRankData[0]['wins']
        summonerRankInfo["Losses"] = userRankData[0]['losses']
        return summonerRankInfo

    def storeUserInfo(self):
        """function to store the information about the summoner"""
        # use getUserInfo and getUserRankInfo, use them to write to a file.
        # seperate files or the same? both?
        filenameInfo = f"data/{self.summonerName}/{self.summonerName}Info.json"
        filenameRankInfo = f"data/{self.summonerName}/{self.summonerName}RankInfo.json"
        filenameFullInfo = f"data/{self.summonerName}/{self.summonerName}FullInfo.json"

        os.mkdir(f"data/{self.summonerName}")

        summonerInfo = self.getUserInfo()
        summonerRankInfo = self.getUserRankInfo()
        fullSummonerInfo = {**summonerInfo, **summonerRankInfo}
        with open(filenameInfo, 'w') as f:
            json.dump(summonerInfo, f, indent=4)
        
        with open(filenameRankInfo, 'w') as f:
            json.dump(summonerRankInfo, f, indent=4)

        with open(filenameFullInfo, 'w') as f:
            json.dump(fullSummonerInfo, f, indent=4)
        
# program loop
def main():
    summonerRajiv = UserInfo("Rajiv")

    userInfo = summonerRajiv.getUserInfo()
    userRankinfo = summonerRajiv.getUserRankInfo()

    for k,v in userInfo.items():
        print(f"{k}: {v}")
    
    for k,v in userRankinfo.items():
        print(f"{k}: {v}")
    
    summonerRajiv.storeUserInfo()

if __name__ == "__main__":
    main()
