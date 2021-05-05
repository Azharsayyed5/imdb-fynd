from typing import Optional, Dict, List
import datetime
from pydantic import BaseModel, Field

class GenericResponse(BaseModel):
    data: Optional[List[Dict]]
    code: Optional[int]
    message: Optional[str]

class MoviesSchema(BaseModel):
    director: str = Field(...)
    genre: List[str] = Field(...)
    imdb_score: int = Field(...)
    name: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "99popularity":99,
                "director": "Cristopher nolan",
                "genre": ["thriller", "action"],
                "imdb_score": 9.6,
                "name": "The dark knight"
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data] if type(data) != list else data,
        "code": 200,
        "message": message,
    }

