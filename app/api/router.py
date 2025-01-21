from fastapi import APIRouter
from app.api.routers import user_router, posts_router


api_router = APIRouter()
api_router.include_router(user_router.router, prefix="/users", tags=["users"])
api_router.include_router(posts_router.router, prefix="/posts", tags=["posts"])


