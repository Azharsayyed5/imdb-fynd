import motor.motor_asyncio
from bson.objectid import ObjectId
import os
import sys
from .config import MONGO_PASSWORD, MONGO_HOST, MONGO_USER, MONG_DATABASE

MONGO_DETAILS = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/{MONG_DATABASE}?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.myFirstDatabase
