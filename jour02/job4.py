import mysql.connector

connect_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Rootp54",
    db = "laplateforme")

cursor = connect_db.cursor()

request_sql = "SELECT nom, capacite FROM salle"

cursor.execute(request_sql)

salles = cursor.fetchall()

for s in salles:
    print(s)

cursor.close()
connect_db.close()