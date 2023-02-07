import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='miskan',
    password='salisana',
    autocommit= True
)

def hae_maakoodilla(maakoodi):
    sql = 'SELECT type FROM airport, country'
    sql += ' WHERE country.iso_country="' + maakoodi + '"'
    #print(sql)
    sql1 = 'SELECT type FROM airport, country'
    sql1 += ' WHERE country.iso_country="' + maakoodi + '"AND airport.type = '"large_airport"''
    sql2 = 'SELECT type FROM airport, country'
    sql2 += ' WHERE country.iso_country="' + maakoodi + '"AND airport.type = '"small_airport"''
    sql3 = 'SELECT type FROM airport, country'
    sql3 += ' WHERE country.iso_country="' + maakoodi + '"AND airport.type = '"heliport"''
    kursori = yhteys.cursor()
    kursori.execute(sql)
    haku = kursori.fetchall()
    #print(haku)
    print(f'Isoja lentokenttiä on {len(sql1)}')
    print(f'Pieniä lentokenttiä on {len(sql2)}')
    print(f'Helikopterikenttiä on {len(sql3)}')

maakoodi = input('Anna maan maakoodi: ')
hae_maakoodilla(maakoodi)
