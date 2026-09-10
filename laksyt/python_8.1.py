import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Beslan1007',
         autocommit=True
         )

icao = input("Anna lentoaseman ICAO-koodi: ").strip().upper()

kutsukortti = yhteys.cursor()
sql = "SELECT name, municipality FROM airport WHERE ident = %s;"
kutsukortti.execute(sql, (icao,))
tulos = kutsukortti.fetchone()

if tulos:
    print(f"Lentokenttä: {tulos[0]}")
    print(f"Sijaintikunta: {tulos[1]}")
else:
    print("Lentokenttää ei löytynyt annetulla ICAO-koodilla.")

yhteys.close()