from fastapi import FastAPI, HTTPException
from api.user import router as user_router

app = FastAPI()

app.add_api_route("/api/v1/user", user_router)

#app.include_router(user_router, prefix="/api/v1")