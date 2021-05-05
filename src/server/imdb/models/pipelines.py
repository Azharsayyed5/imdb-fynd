search_pipeline = [
    {
        '$project': {
            '_id': {
                '$toString': '$_id'
            }, 
            '99popularity': 1, 
            'director': 1, 
            'genre': 1, 
            'imdb_score': 1, 
            'name': 1
        }
    }
]