import urllib2
import json
from datetime import datetime
from appcode.bestsellers.bestsellers_app.models import Bestseller, BookList
from appcode.bestsellers.book.Book import Book

#TODO: use Bestseller instead of Book - TEST!!!
#TODO: make two services: BestsellerService and BookListService
#TODO: move cache + db access methods for list to the second service
#TODO: one time script/method to load list into db, then just retrieve into cache
#TODO: primary key for bestseller books needs to be title+author+booklist+date? -> multiple column key or hash it


class NytBestsellerService:
    __baseUrl__ = "http://api.nytimes.com/svc/books/v2/lists/{Date}{ListName}.json?api-key={ApiKey}"
    __allListsUrl__ = "http://api.nytimes.com/svc/books/v2/lists/names.json?api-key={ApiKey}"
    __listDict__ = {}

    def __init__(self, key):
        self.key = key

    def GetJsonAllBookLists(self):
        bookLists = []
        req = self.__allListsUrl__.format(ApiKey=self.key)
        try:
            result = urllib2.urlopen(req)
            lists = json.load(result)["results"]

            for list in lists:
                listKey = list["list_name"].replace(' ', '-').lower()
                displayName = list["display_name"]
                # self.__listDict__[listKey] = list["display_name"]

                bookList = BookList(ListKey=listKey,
                                    DisplayName=displayName)

                bookLists.append(bookList)

            return bookLists

        except urllib2.URLError, e:
            print(e)

    def JsonResultsToBestsellers(self, results):
        bestsellers = []
        bookListName = Bestseller.objects.get_or_create(ListKey=results["list_name"])

        for book in results:
            title = book["book_details"][0]["title"]
            author = book["book_details"][0]["author"]
            isbn = book["book_details"][0]["primary_isbn13"]
            imageUrl = book["book_details"][0]["book_image"]
            bestsellerDate = datetime.strptime(book["bestsellers_date"], "%Y-%m-%d").date()
            rank = book["rank"]

            bs = Bestseller(Title=title,
                            Author=author,
                            Isbn=isbn,
                            ImageUrl=imageUrl,
                            BestsellerDate=bestsellerDate,
                            Rank=rank,
                            BookList=bookListName)

            bestsellers.append(bs)

        return bestsellers

    def GetJsonList(self, listName):
        req = self.__baseUrl__.format(Date="", ListName=listName, ApiKey=self.key)
        try:
            result = urllib2.urlopen(req)
            return json.load(result)
        except urllib2.URLError, e:
            print(e)