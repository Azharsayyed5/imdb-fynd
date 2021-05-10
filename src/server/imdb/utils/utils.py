import sys
import os
import copy
from pathlib import Path
from fastapi import HTTPException
sys.path.append(os.path.dirname(Path(os.path.abspath(__file__)).parent.parent.parent))
from server.imdb.models.pipelines import (
    pipeline_example
)


def build_pipeline(search, genre, p_srange, p_erange, s_srange, s_erange, sortby, orderby, limit, offset):

    """Build and generate mongodb aggregation pipeline based on received query params

    Raises:
        HTTPException: `STATUS 400`, Invalid query params

    Returns:
       list: MongoDB Aggregation Pipeline
    """

    pipeline = copy.deepcopy(pipeline_example)
    if search:
        pipeline[0]["$match"]["$text"]["$search"] = search

    if not search:
        del pipeline[0]["$match"]["$text"]
    
    if genre:
        genres = [ch.capitalize() for ch in genre.strip().split(",")]
        pipeline[0]["$match"]["genre"]["$in"] = genres
    
    if not genre:
        del pipeline[0]["$match"]["genre"]

    if p_srange.isdigit() and p_erange.isdigit():
        pipeline[0]["$match"]["popularity"]["$gte"] = int(p_srange)
        pipeline[0]["$match"]["popularity"]["$lte"] = int(p_erange)

    if p_srange.isdigit() or p_erange.isdigit():
        if (not p_srange.isdigit()) or (not p_erange.isdigit()):
            del pipeline[0]["$match"]["popularity"]
            raise HTTPException(status_code=400, detail="Send start and end range for popularity filtering", headers={"X-Error": "Query Failed"})

    if s_srange.isdigit() and s_erange.isdigit():
        pipeline[0]["$match"]["imdb_score"]["$gte"] = int(s_srange)
        pipeline[0]["$match"]["imdb_score"]["$lte"] = int(s_erange)

    if s_srange.isdigit() or s_erange.isdigit():
        if (not s_srange.isdigit()) or (not s_erange.isdigit()):
            del pipeline[0]["$match"]["imdb_score"]
            raise HTTPException(status_code=400, detail="Send start and end range for IMDB Score filtering", headers={"X-Error": "Query Failed"})

    if orderby:
        order = 1 if (orderby == "asc") else -1
        pipeline[1]["$sort"]["_id"] = order 

    if sortby:
        if sortby not in ("imdb_score", "popularity"):
            raise HTTPException(status_code=400, detail="Failed, Sorting only works on `imdb_score` and `popularity`.", headers={"X-Error": "Query Failed"})
        pipeline[1]["$sort"][sortby] = pipeline[1]["$sort"].pop("_id")
    
    if not limit:
        pipeline.pop(2)
    else:
        pipeline[2]["$limit"] = limit

    if offset == 0:
        raise HTTPException(status_code=400, detail="Offset cannot be zero, send positive integer greater than zero.", headers={"X-Error": "Query Failed"})

    if offset:
        skip = {
            '$skip': offset
            }
        pipeline.insert(2, skip)

    return pipeline
