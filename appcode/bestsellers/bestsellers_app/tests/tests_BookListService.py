import urllib2
import json
import os
from django.utils import unittest
import mock
from bestsellers_app.nyt.BookListService import BookListService
from bestsellers_app.models import BookList


class TestBookListService(unittest.TestCase):
    def setUp(self):
        cd = os.path.dirname(os.path.abspath(__file__))
        nd = os.path.dirname('../nyt/nyt.keys')
        fn = os.path.join(cd,nd)
        fn = os.path.join(fn, 'nyt.keys')
        with open(fn) as f:
            self.apikey = json.load(f)['key']
        self.bookListService = BookListService("FakeAPIKey!")

    def test_GetJsonAllBookLists_ReturnsEmptyListIfWrongAPIKey(self):
        result = self.bookListService.GetJsonAllBookLists()
        self.assertEqual(result, [], "GetJsonAllBookLists should return empty list for wrong API key or url")

    def test_GetJsonAllBookLists_ReturnsListWithCorrectAPIKey(self):
        bookListService = BookListService(self.apikey)
        result = bookListService.GetJsonAllBookLists()
        self.assertTrue(len(result) > 0)

    def test_ParseJsonAllBookLists_ReturnsEmptyListIfEmptyInput(self):
        parsed = self.bookListService.ParseJsonAllBookLists([])
        self.assertEqual(parsed, [], "Empty input to ParseJsonAllBookLists should return empty list")

    def test_ParseJsonAllBookLists_ParsesCorrectly(self):
        fakeJson = self.__getFakeJsonBookList__()
        print(fakeJson)
        fakeResults = fakeJson["results"]
        parsed = self.bookListService.ParseJsonAllBookLists(fakeResults)
        print parsed[1].__dict__
        for bookList in parsed:
            self.assertIsInstance(bookList,BookList, "Parsed results should be returned as BookList objects")
            self.assertEqual(bookList.ListKey.lower(), bookList.ListKey, "ListKey should have no uppercase letters")
            self.assertEqual(bookList.ListKey.count(' '), 0, "ListKey should have no spaces")

    #Helpers
    def __getFakeJsonBookList__(self):
        return {
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