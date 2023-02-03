import sqlite3 as sql

connection = sql.connect("gta.db")
cursor = connection.cursor()

# cursor.execute("create table gta (year integer, name text, city text)")

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

# cursor.executemany("insert into gta values (?,?,?)", release_list)

for row in cursor.execute("select * from gta"):
    print(row)
print("*********************")

cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)
print("*********************")

# cursor.execute("create table city (gta_city text, real_city text)")

# cursor.execute("insert into city values (?,?)", ("Liberty City", "New York"))

cursor.execute("select * from city where gta_city=:c", {"c": "Liberty City"})

city_search = cursor.fetchall()

print(city_search)
print("*********************")

for i in gta_search:
    adjusted = [city_search[0][1] if value == city_search[0][0] else value for value in i]
    print(adjusted)

connection.commit()

connection.close()
