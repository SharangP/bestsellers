import json
from appcode.bestsellers.nyt import BestsellerService, BookListService


#load api keys
with open('bestsellers/nyt/nyt.keys') as f:
    nytkeys = json.load(f)

bestsellerService = BestsellerService(nytkeys['key'])
bookListService = BookListService
results = bestsellerService.GetJsonList('hardcover-fiction')['results']
print(bestsellerService.LoadListIntoBooks(results))
bookLists = bookListService.GetJsonAllBookLists()
print(bookLists)