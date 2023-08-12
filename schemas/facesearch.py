from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FaceSearch(BaseModel):
    face: str

class Face(FaceSearch):
    searched_at: datetime=datetime.now()