from fastapi import FastAPI
from app.middleware.jwt.jwt_middleware import JWTMiddleware
from app.middleware.logging.logging_middleware import LoggingMiddleware

def register_middlewares(app: FastAPI):
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(JWTMiddleware)