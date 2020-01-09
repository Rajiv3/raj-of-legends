import os
from fileStoragePaths import dataStoragePath

class FileStorage:
    """class to manage where the data files are to be stored"""
    # use the path module

    def __init__(self):
        self.dataStoragePath = dataStoragePath
        self.staticDataStoragePath = f"{self.dataStoragePath}/staticData"

    def makePath(self, pathname):
        """make the path if it does not exist"""
        if not os.path.exists(f"{pathname}"):
            os.makedirs(f"{pathname}")
