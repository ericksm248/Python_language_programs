import requests

data = 100
versiondata = 2
url = "https://pokeapi.co/api/v"+str(versiondata)+"/pokemon?limit="+str(data)

response = requests.get(url)

for pokemon in response.json()["results"]:
    print(pokemon["name"])
