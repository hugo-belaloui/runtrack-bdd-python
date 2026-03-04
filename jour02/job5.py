import mysql.connector

connect_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Rootp54",
    db = "laplateforme"
    )

cursor = connect_db.cursor()

request = "SELECT SUM(superficie) FROM etage"

cursor.execute(request)

result_sum = cursor.fetchone()
result_suming = result_sum[0]

print(f"La sueprficie de La Plateforme est de {(result_suming)} m2")

cursor.close()
connect_db.close()