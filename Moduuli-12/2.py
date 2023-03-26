import requests
Paikkakunta = input("Syötä paikkakunta: ")
Linkki = 'https://api.openweathermap.org/data/2.5/forecast?id=524901&appid=66a8ced379abdb82a75e1e039410544c&q=%22+Paikkakunta'
try:
    pyyntö = requests.get(Linkki).json()
    lämpötila = pyyntö['list'][0]['main']['temp']
    säätila = pyyntö['list'][0]['weather'][0]['description']
    celsius = lämpötila - 272,15
    print(f"Lämpötila: {celsius[0]:.0f}°C\nSäätila: {säätila}")
except:
    print("Virheellinen paikkakunta!")