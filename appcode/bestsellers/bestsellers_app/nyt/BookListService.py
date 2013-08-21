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
        req = self.__allListsUrl__.format(ApiKey=self.__key__)
        try:
            jsonResponse = urllib2.urlopen(req)
            results = json.load(jsonResponse)["results"]
        except urllib2.URLError, e:
            print(e)
            return results

    def ParseJsonAllBookLists(self, bookLists):
        """
        Parses JSON list of all book lists into list of BookList
        :param bookLists Json list of all book lists from NYT api
        :return: list<bookList>
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