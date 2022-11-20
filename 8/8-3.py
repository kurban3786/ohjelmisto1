import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='username',
         password='password',
         autocommit=True
         )

icao = input("icao koodi?")
sql = f"SELECT name, municipality FROM airport where ident = '" + icao + "'"
cursor = yhteys.cursor()
cursor.execute(sql)
result = cursor.fetchall()
print(result)
for rivi in result:
    print(f"{rivi[0]}", rivi[1])

"""
    lat_1 = rivi[0]
    lon_1 = rivi[1]
    """








#print(geopy.distance.distance(airport_1, airport_2).km)