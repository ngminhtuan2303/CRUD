#main
from fastapi import FastAPI
from api.user import router


app = FastAPI()

app.include_router(router)