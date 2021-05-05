import sys
import os
from pathlib import Path
sys.path.append(os.path.dirname(Path(os.path.abspath(__file__)).parent.parent.parent))
from fastapi import APIRouter, Body, Request, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from server.imdb.models.schema import (
    MoviesSchema, GenericResponse, ResponseModel
)
from server.imdb.models.database import (
    create_document, fetch_documents_all, update_document
)
from server.auth.auth_handler import signJWT, decodeJWT
from server.auth.auth_bearer import JWTBearer
from server.config import EXCEPTION_RESPONSE

router = APIRouter()
Auth_handler = JWTBearer(["admin"])


@router.get("/movies", response_description="", response_model=GenericResponse)
async def search_movies():

    """[summary]

    Returns:
        [type]: [description]
    """

    data = await fetch_documents_all()
    return ResponseModel(data, "Success")


@router.post("/movies", dependencies=[Depends(Auth_handler)], response_description="", response_model=GenericResponse)
async def add_movies(data: MoviesSchema):

    """[summary]

    Raises:
        HTTPException: [description]

    Returns:
        [type]: [description]
    """
    
    try:
        movie = await create_document(data)
        return ResponseModel(movie, "Successfully Added The Movie")
    except Exception as GeneralException:
        print(f"add_movies API - {GeneralException}")
        raise HTTPException(status_code=500, detail=EXCEPTION_RESPONSE, headers={"X-Error": EXCEPTION_RESPONSE})


@router.put("/movies/{movie_id}", dependencies=[Depends(Auth_handler)], response_description="", response_model=GenericResponse)
async def update_movies(movie_id: str, data: MoviesSchema):
    data = update_document(movie_id, data)
    if not data:
        raise HTTPException(status_code=404, detail=f"Document with id {movie_id} does not exist", headers={"X-Error": "Movie update failed"})
    return ResponseModel(data, "Successfully Updated The Movie ")


@router.delete("/movies", dependencies=[Depends(Auth_handler)], response_description="", response_model=GenericResponse)
async def delete_movies():
    return ResponseModel([], "OK")
