import uvicorn
from fastapi import FastAPI
from app.api.router import api_router
from app.middleware.middleware import register_middlewares
import app.db.mysql.mysql

app = FastAPI()
app.include_router(api_router)
register_middlewares(app)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, reload=True)