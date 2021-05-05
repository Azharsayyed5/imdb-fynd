import sys
import os
from pathlib import Path
sys.path.append(os.path.dirname(Path(os.path.abspath(__file__)).parent.parent.parent))
from server.connections import database
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from server.imdb.models.pipelines import search_pipeline

# Get collection from database instance
collection = database.get_collection("movies")

# Add New Movie
async def create_document(doc_data: dict) -> dict:

    """Create a single IMDB Movie document in movies collection.

    Returns:
        Dict: New Movie detail
    """

    doc = jsonable_encoder(doc_data)
    doc = await collection.insert_one(doc)
    new_doc = await collection.find_one({"_id": doc.inserted_id}, projection={'_id': False})
    return new_doc

async def fetch_documents_all() -> list:

    """Fetch all documents from movies collection 

    Returns:
        List: List of movies
    """

    data = []
    async for doc in collection.aggregate(search_pipeline):
        data.append(doc)
    return data


async def update_document(_id:str, doc_data: dict) -> dict:

    """update a single IMDB Movie document in movies collection.

    Returns:
        Dict: updated Movie detail
    """

    doc = jsonable_encoder(doc_data)
    doc = await collection.replace_one({'_id': ObjectId(_id)}, doc)
    if doc.modified_count == 0:
        return False
    new_doc = await collection.find_one({"_id": ObjectId(_id)}, projection={'_id': False})
    return new_doc


async def delete_document(_id:str) -> bool:
    """[summary]

    Args:
        _id (str): [description]

    Returns:
        bool: [description]
    """

    doc = await collection.delete_one({'_id': ObjectId(_id)})
    return True