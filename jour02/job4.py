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

cursor = db_connect.cursor()

request_sql = "SELECT nom, capacite FROM salle"

cursor.execute(request_sql)

salles = cursor.fetchall()

for s in salles:
    print(s)

cursor.close()
db_connect.close()