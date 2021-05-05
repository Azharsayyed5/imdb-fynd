import sys
import os
import copy
from pathlib import Path
from fastapi import HTTPException
sys.path.append(os.path.dirname(Path(os.path.abspath(__file__)).parent.parent.parent))
from server.imdb.models.pipelines import (
    pipeline_example
)


def build_pipeline(search, genre, p_srange, p_erange, s_srange, s_erange, sortby, orderby):
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

    if (not p_srange.isdigit()) or (not p_erange.isdigit()):
        del pipeline[0]["$match"]["popularity"]
        # raise HTTPException(status_code=500, detail="popularity start or end range is not valid, send numerical values for both", headers={"X-Error": "Query Failed"})

    if s_srange.isdigit() and s_erange.isdigit():
        pipeline[0]["$match"]["imdb_score"]["$gte"] = int(s_srange)
        pipeline[0]["$match"]["imdb_score"]["$lte"] = int(s_erange)

    if (not s_srange.isdigit()) or (not s_erange.isdigit()):
        del pipeline[0]["$match"]["imdb_score"]
        # raise HTTPException(status_code=500, detail="IMDB Score start or end range is not valid, send numerical values for both", headers={"X-Error": "Query Failed"})

    if sortby:
        order = 1 if (orderby == "asc") else -1
        pipeline[1]["$sort"][sortby] = pipeline[1]["$sort"].pop("_id")
        pipeline[1]["$sort"][sortby] = order 

    return pipeline
