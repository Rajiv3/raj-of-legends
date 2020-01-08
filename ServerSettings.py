from APIKey import api_key
class ServerSettings:
    """class to decide the server and API URLs"""
    def __init__(self, server = 'na1'):
        """Initialize the server settings"""
        self.server = server
        self.api_prefix = f"https://{self.server}.api.riotgames.com"
        self.api_suffix = f"api_key={api_key}"

        """below is links to API calls"""
        self.apiRankedStatsSummonerName = f"/lol/league/v4/entries/by-summoner/"
        self.apiPlayerSummonerName = f"/lol/summoner/v4/summoners/by-name/"
        self.apiMatchlistAccountId = f"/lol/match/v4/matchlists/by-account/"

        """below is links to ddragon calls"""
        self.dragonChampJson = f"https://ddragon.leagueoflegends.com/cdn/9.24.2/data/en_US/champion.json"
