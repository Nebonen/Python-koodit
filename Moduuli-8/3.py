import mysql.connector
from geopy.distance import distance

yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='miskan',
    password='salisana',
    autocommit= True
)

def lentokentat_tiedot(icao_koodi1, icao_koodi2):
    sql1 = 'SELECT ident, latitude_deg, longitude_deg FROM airport WHERE ident ="' + icao_koodi1 + '"'
    sql2 = 'SELECT ident, latitude_deg, longitude_deg FROM airport WHERE ident ="' + icao_koodi2 + '"'
    kursori = yhteys.cursor()
    kursori.execute(sql1, (icao_koodi1, icao_koodi2))
    kursori.execute(sql2, (icao_koodi1, icao_koodi2))
    tulos = kursori.fetchall()
    return tulos

def laske_etaisyys(eka, toka):
    ensimmainen = lentokentat_tiedot(eka)
    toinen = lentokentat_tiedot(toka)
    return distance.distance((ensimmainen['latitude_deg'], ensimmainen['longitude_deg']), (toinen['latitude_deg'], toinen['longitude_deg'])).km

icao_koodi1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao_koodi2 = input("Anna toisen lentokentän ICAO-koodi: ")
etaisyys = laske_etaisyys()
