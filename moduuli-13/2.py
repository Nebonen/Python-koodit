import mysql.connector
from flask import Flask, request


yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='miskan',
    password='salisana',
    autocommit= True
)

app = Flask(__name__)
@app.route('/kentta/<icao_koodi>')
def kentta(icao_koodi):
    sql = 'SELECT name, municipality, ident FROM airport'
    sql += ' WHERE ident="' + icao_koodi + '"'
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    haku = kursori.fetchall()
    print(haku)

    vastaus = {
        haku
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port='3000', debug=True)