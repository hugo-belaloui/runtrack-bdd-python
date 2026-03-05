import mysql.connector
import os 
import dotenv

dotenv.load_dotenv()
db_connect = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    db = os.getenv("DB_NAME")
    )   

#GET A CURSOR 
#OBJECT TO SEND REQUESTS 
cursor = db_connect.cursor()

request_sql = "SELECT * FROM etudiant"
cursor.execute(request_sql)

etudiants = cursor.fetchall()

for e in etudiants:
    print(e)

cursor.close()
db_connect.close()