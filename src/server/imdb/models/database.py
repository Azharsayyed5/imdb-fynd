from server.connections import database
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

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