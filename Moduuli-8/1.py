import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='miskan',
    password='salisana',
    autocommit= True
)

def hae_icao_koodi(icao_koodi):
    sql = 'SELECT name, municipality FROM airport'
    sql += ' WHERE ident="' + icao_koodi + '"'
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    haku = kursori.fetchall()
    print(haku)

icao_koodi = input('Anna lentoaseman icao-koodi: ')
hae_icao_koodi(icao_koodi)
