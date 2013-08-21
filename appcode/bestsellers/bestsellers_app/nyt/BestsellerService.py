import urllib2
import json
from datetime import datetime
from appcode.bestsellers.bestsellers_app.models import Bestseller

#TODO: use Bestseller instead of Book - TEST!!!
#TODO: one time script/method to load list into db, then just retrieve into cache
#TODO: primary key for bestseller books needs to be title+author+booklist+date? -> multiple column key or hash it


class BestsellerService:
    __baseUrl__ = "http://api.nytimes.com/svc/books/v2/lists/{Date}{ListName}.json?api-key={ApiKey}"
    __listDict__ = {}

    def __init__(self, key):
        self.__key__ = key

    def ParseJsonBestsellersByList(self, listResult):
        """
        Parses json bestseller list into list of Bestseller
        :param listResult: JSON bestseller list from NYT api
        :return: list<Bestseller>
        """
        bestsellers = []
        bookListName = Bestseller.objects.get(ListKey=listResult["list_name"])

        for book in listResult:
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

    def GetJsonBestsellersByList(self, listKey):
        """
        Gets bestsellers for book list from NYT api
        :param listKey: key of book list
        :return: JSON result
        """
        req = self.__baseUrl__.format(Date="", ListName=listKey, ApiKey=self.__key__)
        try:
            result = urllib2.urlopen(req)
            return json.load(result)
        except urllib2.URLError, e:
            print(e)