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

request = "SELECT SUM(capacite) FROM salle"

cursor.execute(request)

sum_tuple = cursor.fetchone()
sum_dec = sum_tuple[0]

print(f"La capacité de toutes les salles est de : {sum_dec}")

cursor.close()
db_connect.close()