#main
from fastapi import FastAPI
from api.user import router
from fastapi.middleware.cors import CORSMiddleware
# from milvus_collection import user
app = FastAPI()

app.include_router(router)

# @app.on_event("startup")
# def init_vector_db():
#     user.create_collections_if_not_exist()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)