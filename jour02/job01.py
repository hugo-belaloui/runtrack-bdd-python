import mysql.connector

#CONNECT TO DB 
connect_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Rootp54",
    db = "laplateforme")

#GET A CURSOR 
#OBJECT TO SEND REQUESTS 
cursor = connect_db.cursor()

request_sql = "SELECT * FROM etudiant"
cursor.execute(request_sql)

etudiants = cursor.fetchall()

for e in etudiants:
    print(e)

cursor.close()
connect_db.close()