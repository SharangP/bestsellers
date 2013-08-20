import json


#load api keys
from appcode.bestsellers.bestsellers_app.nyt import BookListService, BestsellerService

with open('bestsellers/bestsellers_app/nyt/nyt.keys') as f:
    nytkeys = json.load(f)

bestsellerService = BestsellerService(nytkeys['key'])
bookListService = BookListService
results = bestsellerService.GetJsonList('hardcover-fiction')['results']
print(bestsellerService.LoadListIntoBooks(results))
bookLists = bookListService.GetJsonAllBookLists()
print(bookLists)