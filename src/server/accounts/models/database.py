import sys
import os
from pathlib import Path
sys.path.append(os.path.dirname(Path(os.path.abspath(__file__)).parent.parent.parent))
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

# Get collection from database instance
collection = database.get_collection("accounts")

# Database operations

async def fetch_document(parameters: dict, hashed_password=False) -> dict:

    """Fetch single document from accounts collection based on user parameters passed

    Returns:
        Dict: User account detail
    """

    project = {'_id': False} if hashed_password else {'_id': False, 'hashed_password': False}
    user = await collection.find_one(parameters, projection=project)
    return user

async def fetch_documents_all() -> list:

    """Fetch all documents from accounts collection 

    Returns:
        List: List of user details
    """

    data = []
    async for doc in collection.find({}, projection={'_id': False, 'hashed_password': False}):
        data.append(doc)
    return data

async def create_document(doc_data: dict) -> dict:

    """Create a single user document in accounts collection upon new user registration

    Returns:
        Dict: User account detail
    """

    hashed_password = get_password_hash(doc_data.password)
    user_in_db = jsonable_encoder((UserInDB(
        **doc_data.dict(), hashed_password=hashed_password, user_id=str(uuid.uuid1()), role='admin'
        )))
    doc = await collection.insert_one(user_in_db)
    new_doc = await collection.find_one({"_id": doc.inserted_id}, projection={'_id': False, 'hashed_password': False})
    return new_doc