# IMDB FYND
Built and documented with `FASTAPI` and `OPENAPI` Standard and with latest python version and for database layer `MongoDB` is used with python's asynchrnous driver `motor`

# Heroku Live Link
- LINK Doc `http://imdb-fynd-in.herokuapp.com/docs`
- LINK Redoc `http://imdb-fynd-in.herokuapp.com/redoc`

# To RUN APP

1. Install `requirements` with latest PIP version
2. From `/src` directory RUN `python3 main.py`
3. Open browser and GOTO `http://127.0.0.1:8000/docs` for `API` documentaion and `TESTING` the APIs

# To RUN Tests

1. From `/src` directory RUN `pytest test.py`

# ENDPOINTS

- Admin
    - Signup
        - `http://imdb-fynd-in.herokuapp.com/v1/accounts/signup` - `POST`

    - Login
        - `http://imdb-fynd-in.herokuapp.com/v1/accounts/login` - `POST`

    - Account details
        - `http://imdb-fynd-in.herokuapp.com/v1/accounts/me` - `GET`

    - Add Movie
        - `http://imdb-fynd-in.herokuapp.com/v1/imdb/movies` - `POST`

    - Update Movie
        - `http://imdb-fynd-in.herokuapp.com/v1/imdb/movies` - `PUT`

    - Delete Movie
        - `http://imdb-fynd-in.herokuapp.com/v1/imdb/movies` - `Delete`

    - View/Search Movies
        - `http://imdb-fynd-in.herokuapp.com/v1/imdb/movies` - `GET`

- User
    - View/Search Movies
        - `http://imdb-fynd-in.herokuapp.com/v1/imdb/movies` - `GET`

- Movie Search Guide
    - Search by movie or directors name
        - `http://imdb-fynd-in.herokuapp.com/v1/imdb/movies?search=batman`
        - `http://imdb-fynd-in.herokuapp.com/v1/imdb/movies?search=christopher%20nolan`
    
    - Filter by genre
        - `http://imdb-fynd-in.herokuapp.com/v1/imdb/movies?genre=action`
        - `http://imdb-fynd-in.herokuapp.com/v1/imdb/movies?genre=thriller`
        - `http://imdb-fynd-in.herokuapp.com/v1/imdb/movies?genre=action,thriller`