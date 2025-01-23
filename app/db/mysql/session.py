from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# MySQL 연결 URL
SQLALCHEMY_DATABASE_URL = settings.MYSQL_DB_URL

# SQLAlchemy 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DB 세션을 가져오는 함수
def get_db():
    db = SessionLocal()
    try:
        yield db  # DB 세션을 요청에 맞게 전달
    finally:
        db.close()  # 세션