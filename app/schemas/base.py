# schemas/base.py
from pydantic import BaseModel

class BaseSchema(BaseModel):
    class Config:
        orm_mode = True  # SQLAlchemy 모델을 자동 변환