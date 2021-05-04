from typing import Optional, Dict, List
import datetime
from pydantic import BaseModel, EmailStr, Field

class Response(BaseModel):
    data: List[Dict]
    status: int
    message: str

class Token(BaseModel):
    access_token: str

class UserInDB(BaseModel):
    hashed_password: str
    email: EmailStr = Field(...)
    fullname: str = Field(...)
    user_id: str = Field(...)
    role: str = Field(...)

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data] if type(data) != list else data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(message, error="Bad Request", code=400):
    return {"error": error, "code": code, "message": message}
