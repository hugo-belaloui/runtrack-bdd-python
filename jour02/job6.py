import mysql.connector

db_connect = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="Rootp54",
    db = "laplateforme"
)

cursor = db_connect.cursor()

request = "SELECT SUM(capacite) FROM salle"

cursor.execute(request)

sum_tuple = cursor.fetchone()
sum_dec = sum_tuple[0]

print(f"La capacité de toutes les salles est de : {sum_dec}")

cursor.close()
db_connect.close()