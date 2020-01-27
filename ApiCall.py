from ServerSettings import ServerSettings

class ApiCall:
    """class to call the API"""
    """put more parameters into requests.get()?"""

    def __init__(self, url):
        self.url = url
        self.serverSettings = ServerSettings() 

    def requestApi(self, status = "yes", display = "no", displayType = "no"):
        """Function to call the API"""
        url = f"{self.url}"
        r = requests.get(url)
        printStatusCode(status)
        displayResult(display, r)
        displayType(displayType, r)
        return r

    def printStatusCode(self, status):
        """function to decide if status code should be printed """
        if status = "yes":
            print(f"Status code: {r.status_code}")

    def displayResult(self, display, data):
        """function to decide whether to display results"""
        if display == "yes":
            print(data)
        
    def displayType(self, display, data):
        """function to decide whether to display results type"""
        if display == "yes":
            print(type(data))
