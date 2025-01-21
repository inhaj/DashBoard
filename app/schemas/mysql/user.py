# schemas/user.py
from pydantic import EmailStr
from datetime import datetime
from schemas.base import BaseSchema

# 사용자 생성 요청 스키마
class UserCreate(BaseSchema):  
    email: EmailStr
    password: str

# 사용자 응답 스키마
class UserResponse(BaseSchema):  
    id: int
    email: EmailStr
    created_at: datetime