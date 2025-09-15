from fastapi import FastAPI
import uvicorn
from powervs_backend.config import init_db
from powervs_backend.urls import api_router

app = FastAPI(title="PowerVS Backend")

init_db(app=app)
app.include_router(api_router, prefix="/api")
@app.get('/')
async def root():
    return {'message': 'API is working'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
