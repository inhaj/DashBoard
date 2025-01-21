from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.db.mysql.base import Base  
from app.models.mysql.user import User  

# 데이터베이스 URL
SQLALCHEMY_DATABASE_URL = settings.MYSQL_DB_URL

# 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 테이블 생성
Base.metadata.create_all(bind=engine)