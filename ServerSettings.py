from APIKey import api_key
class ServerSettings:
    """class to decide the server and API URLs"""
    def __init__(self, server = "na1"):
        """Initialize the server settings"""
        self.server = server
        self.api_prefix = f"https://{self.server}.api.riotgames.com"
        self.api_suffix = f"api_key={api_key}"

        """below are links to API calls"""
        self.apiRankedStatsSummonerName = f"/lol/league/v4/entries/by-summoner/"
        self.apiPlayerSummonerName = f"/lol/summoner/v4/summoners/by-name/"
        self.apiMatchlistAccountId = f"/lol/match/v4/matchlists/by-account/"

        """below are links to ddragon calls"""
        self.dragonChampJson = f"https://ddragon.leagueoflegends.com/cdn/10.1.1/data/en_US/champion.json"

        """below are links to static calls"""
        self.staticSeasonsUrl = f"http://static.developer.riotgames.com/docs/lol/seasons.json"
        self.staticQueueIdsUrl = f"http://static.developer.riotgames.com/docs/lol/queues.json"
        self.staticMapsUrl = f"http://static.developer.riotgames.com/docs/lol/maps.json"
        self.staticGameModesUrl = f"http://static.developer.riotgames.com/docs/lol/gameModes.json"
        self.staticGameTypesUrl = f"http://static.developer.riotgames.com/docs/lol/gameTypes.json"
