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

request = "SELECT SUM(superficie) FROM etage"

cursor.execute(request)

result_sum = cursor.fetchone()
result_suming = result_sum[0]

print(f"La sueprficie de La Plateforme est de {(result_suming)} m2")

cursor.close()
db_connect.close()