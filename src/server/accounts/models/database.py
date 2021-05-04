from server.connections import database
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
import uuid
from server.accounts.models.schema import (
     UserInDB
)
from server.accounts.utils.utils import (
    get_password_hash
)

collection = database.get_collection("accounts")

# Database operations

async def fetch_document(parameters: dict, hashed_password=False) -> dict:
    project = {'_id': False} if hashed_password else {'_id': False, 'hashed_password': False}
    user = await collection.find_one(parameters, projection=project)
    return user

async def fetch_documents_all() -> list:
    data = []
    async for doc in collection.find({}, projection={'_id': False, 'hashed_password': False}):
        data.append(doc)
    return data

async def create_document(doc_data: dict) -> dict:
    hashed_password = get_password_hash(doc_data.password)
    user_in_db = jsonable_encoder((UserInDB(
        **doc_data.dict(), hashed_password=hashed_password, user_id=str(uuid.uuid1()), role='user'
        )))
    doc = await collection.insert_one(user_in_db)
    new_doc = await collection.find_one({"_id": doc.inserted_id}, projection={'_id': False, 'hashed_password': False})
    return new_doc