import json
from nyt.NytBestsellerService import NytBestsellerService


#load api keys
with open('nyt/nyt.keys') as f:
    nytkeys = json.load(f)

nyt = NytBestsellerService(nytkeys['key'])
nyt.GetList('sup')
