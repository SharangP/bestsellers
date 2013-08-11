import json
from nyt.NytBestsellerService import NytBestsellerService


#load api keys
with open('nyt/nyt.keys') as f:
    nytkeys = json.load(f)

nyt = NytBestsellerService(nytkeys['key'])
# results = nyt.GetList('hardcover-fiction')['results']
# print(nyt.LoadListIntoBooks(results))
nyt.LoadListOfBookLists()
print(nyt.__listDict__)
