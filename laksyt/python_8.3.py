import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Beslan1007',
         autocommit=True
         )

def hae_koordinaatit(icao):
    kutsukortti = yhteys.cursor()
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s;"
    kutsukortti.execute(sql, (icao,))
    return kutsukortti.fetchone()

icao1 = input("Anna 1. lentokentän ICAO-koodi: ").strip().upper()
icao2 = input("Anna 2. lentokentän ICAO-koodi: ").strip().upper()

sijainti1 = hae_koordinaatit(icao1)
sijainti2 = hae_koordinaatit(icao2)

if sijainti1 and sijainti2:
    # geopy ottaa koordinaatit muodossa (latitude, longitude)
    etaisyys_km = distance(sijainti1, sijainti2).km
    print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {etaisyys_km:.2f} km.")
else:
    print("Toista tai kumpaakaan lentokenttää ei löytynyt tietokannasta.")

yhteys.close()