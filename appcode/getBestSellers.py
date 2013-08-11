import json
from appcode.bestsellers.nyt import NytBestsellerService


#load api keys
with open('bestsellers/nyt/nyt.keys') as f:
    nytkeys = json.load(f)

nyt = NytBestsellerService(nytkeys['key'])
# results = nyt.GetList('hardcover-fiction')['results']
# print(nyt.LoadListIntoBooks(results))
nyt.LoadListOfBookLists()
print(nyt.__listDict__)
