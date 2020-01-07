from APIKey import api_key
class ServerSettings:
    """class to decide the server"""
    def __init__(self, server = 'na1'):
        """Initialize the server settings"""
        self.server = server
        self.api_prefix = f"https://{self.server}.api.riotgames.com"
        self.api_suffix = f"?api_key={api_key}"
