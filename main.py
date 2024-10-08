import traceback
from mongoengine import connect

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

origins = ["*"]  # Replace with your allowed origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_VERSION)

@app.on_event("startup")
async def startup_event():
    try:
        connect(db=settings.DATABASE, alias=settings.DATABASE, host=settings.MONGODB_URI)
    except Exception as e:
        print(f"Connect DB : {str(e)}")
        print(traceback.format_exc())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)