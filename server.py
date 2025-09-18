import logging
import os

import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from core.oauth2_password_bearer import get_oauth2_scheme
from powervs_backend.config import init_db
from powervs_backend.urls import api_router
from core import logging_config

logger = logging.getLogger("fastapi-backend")
oauth2_scheme = get_oauth2_scheme()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = FastAPI(title="PowerVS Backend")

init_db(app=app)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Middleware to log each request and response."""
    try:
        response = await call_next(request)
    except Exception as e:
        logger.error(e)
        logger.exception(f"Unhandled error on {request.url.path}")
        return JSONResponse({"error": "Internal server error"}, status_code=500)
    return response


app.include_router(api_router, prefix="/api")

@app.get('/')
async def root():
    return {'message': 'API is working'}


if __name__ == "__main__":
    uvicorn.run('server:app', host="localhost", port=8001, reload=True)
