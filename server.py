import os

import uvicorn
from fastapi import FastAPI

from core.oauth2_password_bearer import get_oauth2_scheme
from powervs_backend.config import init_db
from powervs_backend.urls import api_router

oauth2_scheme = get_oauth2_scheme()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = FastAPI(title="PowerVS Backend")

init_db(app=app)
app.include_router(api_router, prefix="/api")


@app.get('/')
async def root():
    return {'message': 'API is working'}


if __name__ == "__main__":
    uvicorn.run('server:app', host="localhost", port=8001, reload=True)
