from pydantic import BaseModel
from datetime import datetime


class PostCreate(BaseModel):
    title: str
    content: str
    author_id: str


class PostResponse(BaseModel):
    id: str
    title: str
    content: str
    author_id: str
    created_at: datetime

    class Config:
        orm_mode = True