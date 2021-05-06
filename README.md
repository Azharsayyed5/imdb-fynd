## IMDB FYND
Built and documented with `FASTAPI` and `OPENAPI` Standard and with latest python version and for database layer `MongoDB` is used with python's asynchrnous driver `motor`

## Heroku Live Link
- [🦸 LINK Doc](https://imdb-fynd-in.herokuapp.com/docs)
- [🦸‍♀️ LINK Redoc](https://imdb-fynd-in.herokuapp.com/redoc)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`JWT_SECRET`

`JWT_ALGORITHM`

`MONGO_USER`

`MONGO_PASSWORD`

`MONGO_HOST`

`MONGO_DATABASE`

## Run Locally
Clone the project

```bash
   git clone https://github.com/Azharsayyed5/imdb-fynd/
```

Install requirements and packages

```bash
   python3 -m pip install -r requirements.txt
```

Change directory to `src`

```bash
   cd /src
```

Run below command to start `uvicorn` server

```bash
   python3 main.py
```

## Run Tests

Change directory to `src`

```bash
   cd /src
```

Run below command to run tests

```bash
   pytest test.py
```


## To Scale APP

[Documentation](https://github.com/Azharsayyed5/imdb-fynd/blob/main/scaling_101.txt)

## ENDPOINTS

- Admin
    - Signup
        - `https://imdb-fynd-in.herokuapp.com/v1/accounts/signup` - `POST`

    - Login
        - `https://imdb-fynd-in.herokuapp.com/v1/accounts/login` - `POST`

    - Account details
        - `https://imdb-fynd-in.herokuapp.com/v1/accounts/me` - `GET`

    - Add Movie
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies` - `POST`

    - Update Movie
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies` - `PUT`

    - Delete Movie
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies` - `Delete`

    - View/Search Movies
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies` - `GET`

- User
    - View/Search Movies
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies` - `GET`

## Movie Search Guide
- Search by `movie or directors` name
    - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?search=batman`
    - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?search=christopher%20nolan`

- Filter by `genre`
    - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?genre=action`
    - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?genre=thriller`
    - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?genre=action,thriller`

- Filter by `popularity` range
    - Filter movies which has popularity between 0 to 50
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?p_srange=0&p_erange=50`
    - Filter movies which has popularity between 50 to 100
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?p_srange=50&p_erange=100`

- Filter by `IMDB score` range
    - Filter movies which has IMDB score between 0 to 5
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?s_srange=0&s_erange=5`
    - Filter movies which has IMDB score between 5 to 10
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?s_srange=5&s_erange=10`

- Filter with `popularity and IMDB score` range
    - Filter movies which has IMDB score between 0 to 5 and popularity between 0 to 50
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?s_srange=0&s_erange=5&p_srange=0&p_erange=50`

- Sorting and order
    - Sort by `popularity score` - `Ascending`
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?sortby=popularity&orderby=asc`
    - Sort by `popularity score` - `Descending`
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?sortby=popularity5&orderby=desc`
    - Sort by `IMDB score` - `Ascending`
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?sortby=imdb_score&orderby=asc`
    - Sort by `IMDB score` - `Descending`
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?sortby=imdb_score&orderby=desc`
    - Change default ordering
        - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?orderby=desc`
    - `If sorting and ordering params not passed then by default documents will be sorted in ascending order with ObjectId field`

- Limit
    - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?limit=10`

- Search and filter with everything
    - `https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?search=batman&genre=action&p_srange=0&p_erange=80&s_srange=0&s_erange=10&sortby=imdb_score&orderby=desc&limit=10`
    - Feel free to try different filters
