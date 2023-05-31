from fastapi import FastAPI, HTTPException
from api.user import router as user_router
from datetime import datetime
from uuid import uuid4
from typing import List
from pydantic import BaseModel, validator, EmailStr

app = FastAPI()

app.add_api_route("/api/v1/user", user_router)

