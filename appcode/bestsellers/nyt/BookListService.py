import json
import urllib2
from appcode.bestsellers.bestsellers_app.models import BookList
from django.core.exceptions import ValidationError


class BookListService:
    __allListsUrl__ = "http://api.nytimes.com/svc/books/v2/lists/names.json?api-key={ApiKey}"
    BookListCache = {}

    def __init__(self, key):
        self.__key__ = key

    def GetJsonAllBookLists(self):
        """
        Fetches all booklists from NYT api

        :return: list<bookList>
        """
        bookLists = []
        req = self.__allListsUrl__.format(ApiKey=self.__key__)
        try:
            result = urllib2.urlopen(req)
            bookLists = json.load(result)["results"]

            for bookList in bookLists:
                listKey = bookList["list_name"].replace(' ', '-').lower()
                displayName = bookList["display_name"]
                # self.__listDict__[listKey] = list["display_name"]

                bookList = BookList(ListKey=listKey,
                                    DisplayName=displayName)

                bookLists.append(bookList)

            return bookLists

        except urllib2.URLError, e:
            print(e)

    def BulkSaveBookLists(self, bookLists):
        for bookList in bookLists:
            try:
                BookList.objects.get_or_create(ListKey=bookList.ListKey,
                                               DisplayName=bookList.DisplayName)
            except ValidationError, e:
                print(e)

    def LoadBookListCache(self):
        for bookList in BookList.objects.all():
            self.BookListCache[bookList.ListKey] = bookList.DisplayName