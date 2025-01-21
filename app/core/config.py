# core/config.py
import os

class Settings:
    # MySQL DB 설정
    MYSQL_DB_URL = os.getenv("MYSQL_DB_URL", "mysql+pymysql://username:password@localhost/db_name")
    
    # MongoDB 설정
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "my_database")

settings = Settings()