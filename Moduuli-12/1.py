import requests

pyynto = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyynto)

if vastaus.status_code == 200:
    json_vastaus = vastaus.json()
    vitsi = json_vastaus["value"]
    print(vitsi)
else:
    print(f'Error: {vastaus.status_code}')