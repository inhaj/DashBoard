from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from app.core.logger import logger
import time
import json


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        client_ip = request.client.host
        method = request.method
        path = request.url.path

        logger.info(f"Incoming request: {method} {path} from {client_ip}")
        logger.info(f"Headers: {dict(request.headers)}")

        try:
            request_body = await request.json()
            logger.info(f"Request body: {json.dumps(request_body, indent=2)}")
        except Exception:
            logger.warning("Request body is not a valid JSON or is empty.")

        try:
            response = await call_next(request)
            process_time = time.time() - start_time

            response_body = await response.body()
            try:
                response_json = json.loads(response_body)
                logger.info(f"Response body: {json.dumps(response_json, indent=2)}")
            except json.JSONDecodeError:
                logger.warning("Response body is not a valid JSON.")
            
            logger.info(
                f"Response: {method} {path} | "
                f"Status code: {response.status_code} | "
                f"Process time: {process_time:.2f}s"
            )

            return Response(
                content=json.dumps(response_json),
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type="application/json"
            )
        except Exception as e:
            logger.error(f"Error processing request: {e}")
            raise e