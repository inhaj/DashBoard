# database/mongodb.py
from pymongo import MongoClient
from core.config import settings

# MongoDB 연결 설정
client = MongoClient(settings.MONGODB_URI)
db = client[settings.MONGODB_DB_NAME]