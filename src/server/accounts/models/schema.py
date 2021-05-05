from typing import Optional, Dict, List
import datetime
from pydantic import BaseModel, EmailStr, Field

class GenericResponse(BaseModel):
    data: Optional[List[Dict]]
    code: Optional[int]
    message: Optional[str]

class Token(BaseModel):
    access_token: Optional[str]

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
                "fullname": "Azhar sayyed",
                "email": "arizsayed777@gmail,com",
                "password": "123456"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "arizsayed777@gmail,com",
                "password": "123456"
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
