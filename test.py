import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

db_uri = os.getenv('SQLALCHEMY_DATABASE_URI')

print(f"Database URI: {db_uri}")

try:
    connection = pymysql.connect(
        host='localhost',
        user='local',
        password='12345',
        database='JObS'
    )
    print("Connection successful!")
    connection.close()
except pymysql.MySQLError as e:
    print(f"Error connecting to database: {e}")
