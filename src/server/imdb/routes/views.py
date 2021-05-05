import sys
import os
from pathlib import Path
from bson.objectid import ObjectId
sys.path.append(os.path.dirname(Path(os.path.abspath(__file__)).parent.parent.parent))
from fastapi import APIRouter, Body, Request, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from server.imdb.models.schema import (
    MoviesSchema, GenericResponse, ResponseModel
)
from server.imdb.models.database import (
    create_document, fetch_documents_all, update_document, delete_document
)
from server.auth.auth_handler import signJWT, decodeJWT
from server.auth.auth_bearer import JWTBearer
from server.config import EXCEPTION_RESPONSE

router = APIRouter()
Auth_handler = JWTBearer(["admin"])

def HTTPExceptionResponse(ExceptionRx):
    if hasattr(ExceptionRx, 'detail'):
        raise HTTPException(status_code=ExceptionRx.status_code, detail=ExceptionRx.detail, headers=ExceptionRx.headers)
    else:
        raise HTTPException(status_code=500, detail=EXCEPTION_RESPONSE, headers={"X-Error": EXCEPTION_RESPONSE})


@router.get("/movies", response_description="", response_model=GenericResponse)
async def search_movies():

    """Endpoint to fetch movie records from database with different types of search and sort parameters

    Returns:
        dict: List of movies and its details
    """

    data = await fetch_documents_all()
    return ResponseModel(data, "Success")


@router.post("/movies", dependencies=[Depends(Auth_handler)], response_description="", response_model=GenericResponse)
async def add_movies(data: MoviesSchema):

    """Endpoint to add new movie into the system, before adding the received data into database
    the pydantic validations is performed to check for any missing data or wrong type.

    Raises:
        HTTPException: `STATUS 500`, General Exception

    Returns:
        dict: Added Movie
    """
    
    try:
        movie = await create_document(data)
        return ResponseModel(movie, "Successfully Added The Movie")
    except Exception as GeneralException:
        print(f"add_movies API - {GeneralException}")
        HTTPExceptionResponse(GeneralException)


@router.put("/movies/{movie_id}", response_description="", response_model=GenericResponse)
async def update_movies(movie_id: str, data: MoviesSchema):

    """Update details about a particular movie, before updating the received data into database
    the pydantic validations is performed to check for any missing data or wrong type.

    Raises:
        HTTPException: `STATUS 500`, Invalid Object ID
        HTTPException: `STATUS 404`, Item does not exist

    Returns:
        dict: Updated movie data
    """

    try:
        if not ObjectId.is_valid(movie_id):
            raise HTTPException(status_code=500, detail=f"Invalid ID - {movie_id}", headers={"X-Error": "Invalid Mongo ObjectID"})

        data = await update_document(movie_id, data)
        if not data:
            raise HTTPException(status_code=404, detail=f"Document with id {movie_id} does not exist", headers={"X-Error": "Movie update failed"})
        return ResponseModel(data, "Successfully Updated The Movie")
    except Exception as GeneralException:
        print(f"update_movies API - {GeneralException}")
        HTTPExceptionResponse(GeneralException)


@router.delete("/movies/{movie_id}", response_description="", response_model=GenericResponse)
async def delete_movies(movie_id: str):

    """Endpoint to delete a particular movie details from the database based on movie_id / ObjectId

    Raises:
        HTTPException: `STATUS 500`, Invalid Object ID
        HTTPException: `STATUS 500`, General Exception

    Returns:
        dict: Delete status
    """

    try:
        if not ObjectId.is_valid(movie_id):
            raise HTTPException(status_code=500, detail=f"Invalid ID - {movie_id}", headers={"X-Error": "Invalid Mongo ObjectID"})

        data = await delete_document(movie_id)
        if not data:
            raise HTTPException(status_code=500, detail=f"Failed to Delete - {movie_id}", headers={"X-Error": "Movie deletion failed"})
        return ResponseModel([], "Successfully deleted the movie")
    except Exception as GeneralException:
        print(f"delete_movies API - {GeneralException}")
        HTTPExceptionResponse(GeneralException)


