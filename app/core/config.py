import os
from dotenv import load_dotenv

load_dotenv() 

class Settings:
    # MySQL DB 설정
    MYSQL_DB_URL = os.getenv("MYSQL_DB_URL", "")
    
    # MongoDB 설정
    MONGODB_URI = os.getenv("MONGODB_URI", "")
    MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "")

settings = Settings