from fastapi import FastAPI
from api.user import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/api/v1/user")
