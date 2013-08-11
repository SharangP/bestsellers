import urllib2
import json
from appcode.bestsellers.bestsellers_app.models import Bestseller, BookList
from appcode.bestsellers.book.Book import Book

#TODO: use Bestseller instead of Book
#TODO: make two services: BestsellerService and BookListService
#TODO: move cache + db access methods for list to the second service
#TODO: one time script/method to load list into db, then just retrieve into cache


class NytBestsellerService:
    __baseUrl__ = "http://api.nytimes.com/svc/books/v2/lists/{Date}{ListName}.json?api-key={ApiKey}"
    __allListsUrl__ = "http://api.nytimes.com/svc/books/v2/lists/names.json?api-key={ApiKey}"
    __listDict__ = {}

    def __init__(self, key):
        self.key = key

    def LoadListOfBookLists(self):
        req = self.__allListsUrl__.format(ApiKey=self.key)
        try:
            result = urllib2.urlopen(req)
            lists = json.load(result)["results"]
            for list in lists:
                listKey = list["list_name"].replace(' ', '-').lower()
                self.__listDict__[listKey] = list["display_name"]
        except urllib2.URLError, e:
            print(e)

    def LoadListIntoBooks(self, list):
        bookList = []
        for book in list:
            isbn = book["book_details"][0]["primary_isbn13"]
            title = book["book_details"][0]["title"]
            author = book["book_details"][0]["author"]
            bookList.append(Book(isbn, title, author))
        return bookList

    def GetList(self, listName):
        req = self.__baseUrl__.format(Date="", ListName=listName, ApiKey=self.key)
        try:
            result = urllib2.urlopen(req)
            return json.load(result)
        except urllib2.URLError, e:
            print(e)