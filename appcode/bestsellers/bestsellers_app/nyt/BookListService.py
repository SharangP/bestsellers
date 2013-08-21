import json
import urllib2
from bestsellers_app.models import BookList


class BookListService:
    __allListsUrl__ = "http://api.nytimes.com/svc/books/v2/lists/names.json?api-key={ApiKey}"
    BookListCache = {}

    def __init__(self, key):
        self.__key__ = key

    def GetJsonAllBookLists(self):
        """
        Fetches all booklists from NYT api
        :return: JSON results
        """
        results = []
        url = self.__allListsUrl__.format(ApiKey=self.__key__)
        try:
            hdr = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            }
            req = urllib2.Request(url, headers=hdr)
            jsonResponse = urllib2.urlopen(req)
            results = json.load(jsonResponse)["results"]
            return results
            urllib2.urlopen()
        except urllib2.URLError, e:
            # print(e.fp.read())
            return results

    def ParseJsonAllBookLists(self, bookLists):
        """
        Parses JSON list of all book lists into list of BookList
        :param bookLists Json list of all book lists from NYT api
        :return: [BookList]
        """
        parsedBookLists = []
        for bookList in bookLists:
            listKey = bookList["list_name"].replace(' ', '-').lower()
            displayName = bookList["display_name"]
            parsedBookLists.append(BookList(ListKey=listKey,DisplayName=displayName))
        return parsedBookLists

    def BulkSaveBookLists(self, bookLists):
        for bookList in bookLists:
            try:
                BookList.objects.get_or_create(ListKey=bookList.ListKey,
                                               DisplayName=bookList.DisplayName)
            except Exception as e:
                print(e)
                raise e

    def LoadBookListCache(self):
        for bookList in BookList.objects.all():
            self.BookListCache[bookList.ListKey] = bookList.DisplayName

    def RefreshCache(self):
        jsonResults = self.GetJsonAllBookLists()
        parsedResults = self.ParseJsonAllBookLists(jsonResults)
        if parsedResults:
            self.BulkSaveBookLists(parsedResults)
        if parsedResults and not self.BookListCache:
            self.LoadBookListCache()