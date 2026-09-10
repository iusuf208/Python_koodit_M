import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Beslan1007',
         autocommit=True
         )

maakoodi = input("Anna maakoodi (esim. FI): ").strip().upper()

kutsukortti = yhteys.cursor()
sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type;"
kutsukortti.execute(sql, (maakoodi,))
tulokset = kutsukortti.fetchall()

if tulokset:
    print(f"\nLentokenttien määrä maassa {maakoodi} tyypeittäin:")
    for tyyppi, maara in tulokset:
        print(f"{tyyppi}: {maara} kappaletta")
else:
    print("Kyseisellä maakoodilla ei löytynyt lentokenttiä.")

yhteys.close()