# database/mysql.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

# MySQL 데이터베이스 URL
SQLALCHEMY_DATABASE_URL = settings.MYSQL_DB_URL

# SQLAlchemy 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()