from datetime import datetime
from schemas.base import BaseSchema

class RefreshTokenCreate(BaseSchema):
    user_id: int
    token: str
    expires_at: datetime


class RefreshTokenResponse(BaseSchema):
    id: int
    user_id: int
    token: str
    created_at: datetime
    expires_at: datetime
