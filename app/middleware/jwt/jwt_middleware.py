from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi import status
from app.core.security import verify_token
from app.core.config import settings
from app.core.logger import logger

class JWTMiddleware(BaseHTTPMiddleware):
    async def _unauthorized_response(self):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Invalid authentication credentials"},
            headers={"WWW-Authenticate": "Bearer"}
        )

    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        method = request.method

        for protected_path, methods in settings.AUTH_REQUIRED_PATHS.items():
            if path.startswith(protected_path) and method in methods:
                auth_header = request.headers.get("Authorization")  
                if auth_header is None or not auth_header.startswith("Bearer "):
                    logger.warning(f"Unauthorized request: {method} {path}")
                    return await self._unauthorized_response()
                try:
                    token = auth_header.split(" ")[1]
                    verify_token(token)
                    logger.info(f"Token verified for {method} {path}")
                except Exception as e:
                    logger.error(f"Token verification failed: {e}")
                    return await self._unauthorized_response()
                finally:
                    break
        return await call_next(request)

    