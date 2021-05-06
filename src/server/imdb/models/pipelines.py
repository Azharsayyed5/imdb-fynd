pipeline_example = [
    {
        '$match': {
            '$text': {
                '$search': 'batman'
            }, 
            'genre': {
                '$in': [
                    'Action'
                ]
            }, 
            'popularity': {
                '$gte': 0, 
                '$lte': 80
            }, 
            'imdb_score': {
                '$gte': 0, 
                '$lte': 10
            }
        }
    }, {
        '$sort': {
            '_id': -1
        }
    }, {
        '$limit': 10
    }, {
        '$project': {
            '_id': {
                '$toString': '$_id'
            }, 
            'popularity': 1, 
            'director': 1, 
            'genre': 1, 
            'imdb_score': 1, 
            'name': 1
        }
    }
]