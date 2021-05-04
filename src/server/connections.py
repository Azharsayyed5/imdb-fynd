import motor.motor_asyncio
from bson.objectid import ObjectId
import os
import sys
from .config import MONGO_PASSWORD

MONGO_DETAILS = f"mongodb+srv://root:{MONGO_PASSWORD}@cluster0.vgoq0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.myFirstDatabase
