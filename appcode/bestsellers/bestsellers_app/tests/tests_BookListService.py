import urllib2
from django.utils import unittest
import mock


class TestBookListService(unittest.TestCase):
    def setUp(self):
        urllib2.urlopen = mock.Mock(return_value=self.__getFakeJsonBookList__())

    def test_GetJsonAllBookLists_ReturnsListOfBooks(self):
        pass

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