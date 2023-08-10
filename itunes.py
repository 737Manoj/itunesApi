import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
#sys.exit breaks you out of the entire program unlike break statement which just breaks you out of the loop.

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

o = response.json()
for result in o ["results"]:
    print(result["trackName"])




