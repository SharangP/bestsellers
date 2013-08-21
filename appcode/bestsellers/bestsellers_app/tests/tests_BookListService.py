import urllib2
from django.utils import unittest
import mock
from bestsellers_app.nyt.BookListService import BookListService


class TestBookListService(unittest.TestCase):
    def test_tests(self):
        self.assertEqual(1,1,"1=1 duh")

    def test_GetJsonAllBookLists_ReturnsEmptyListIfWrongAPIKey(self):
        bookListService = BookListService("FakeAPIKey!")
        result = bookListService.GetJsonAllBookLists()
        self.assertEqual(result,{},"GetJsonAllBookLists should return empty list for wrong API key or url")

    #Helpers
    def __getFakeJsonBookList__(self):
        return
        """
            {
               "status":"OK",
               "copyright":"Copyright (c) 2013 The New York Times Company.  All Rights Reserved.",
               "num_results":27,
               "results":[
                  {
                     "list_name":"Combined Print and E-Book Fiction",
                     "display_name":"Combined Print & E-Book Fiction"
                  },
                  {
                     "list_name":"Combined Print and E-Book Nonfiction",
                     "display_name":"Combined Print & E-Book Nonfiction"
                  }
               ]
            }
        """