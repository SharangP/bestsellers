from urllib2 import urlopen
from json import loads


class NytBestsellerService:
    __baseUrl__ = "http://api.nytimes.com/svc/books/v2/lists/{Date}{ListName}.json?&api-key={ApiKey}"

    def __init__(self, key):
        self.key = key

    def GetList(self, listName):
        r = self.__baseUrl__.format(Date="", ListName=listName, ApiKey=self.key)
        print(r)
