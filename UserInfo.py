import requests
from APIKey import api_key

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

# program loop
def main():
    summonerRajiv = UserInfo("Rajiv")

    userInfo = summonerRajiv.getUserInfo()
    userRankinfo = summonerRajiv.getUserRankInfo()

    for k,v in userInfo.items():
        print(f"{k}: {v}")
    
    for k,v in userRankinfo.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
