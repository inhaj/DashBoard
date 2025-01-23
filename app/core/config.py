import os
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv() 

POST = "POST"
GET = "GET"
PUT = "PUT"
DELETE = "DELETE"

class Settings:
    # MySQL DB 설정
    MYSQL_DB_URL = os.getenv("MYSQL_DB_URL", "")
    
    # MongoDB 설정
    MONGODB_URI = os.getenv("MONGODB_URI", "")
    MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "")
    
    #JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY","")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int =  360
    REFRESH_TOKEN_EXPIRE_DAYS:int = 7
    AUTH_REQUIRED_PATHS: Dict[str, List[str]] = {
        "/posts": [POST, PUT, DELETE]
    }
    

settings = Settings