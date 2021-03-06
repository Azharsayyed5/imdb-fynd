# IMDB FYND

Built and documented with `FASTAPI` and `OPENAPI` Standard and with latest python version and for database layer `MongoDB` is used with python's asynchrnous driver `motor`

## Heroku Live Link
[🦸 LINK Doc](https://imdb-fynd-in.herokuapp.com/docs)
[🦸‍♀️ LINK Redoc](https://imdb-fynd-in.herokuapp.com/redoc)

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
git clone https://github.com/Azharsayyed5/imdb-fynd.git
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
        ```http
        POST https://imdb-fynd-in.herokuapp.com/v1/accounts/signup
        ```
        
        Request Body - **JSON**
        Parameter | Type     | Description                |
        | :-------- | :------- | :------------------------- |
        | `fullname` | `string` | **Required**. Full name |
        | `email` | `string` | **Required**. Email address |
        | `password` | `string` | **Required**. Password |
    
    - Login

        ```http
        POST https://imdb-fynd-in.herokuapp.com/v1/accounts/login
        ```
        
        Request Body - **JSON**
        Parameter | Type     | Description                |
        | :-------- | :------- | :------------------------- |
        | `email` | `string` | **Required**. Email address |
        | `password` | `string` | **Required**. Password |

    - Account details

        ```http
        GET https://imdb-fynd-in.herokuapp.com/v1/accounts/me
        ```

    - Add Movie

        ```http
        POST https://imdb-fynd-in.herokuapp.com/v1/imdb/movies
        ```
        
        Request Body - **JSON**
        Parameter | Type     | Description                |
        | :-------- | :------- | :------------------------- |
        | `popularity` | `string` | **Required**. popularity score |
        | `director` | `string` | **Required**. Directors name |
        | `genre` | `list` | **Required**. Genre |
        | `imdb_score` | `string` | **Required**. imdb score |
        | `name` | `string` | **Required**. Movie name |

    - Update Movie
        ```http
        PUT https://imdb-fynd-in.herokuapp.com/v1/imdb/movies/{movie_id}
        ```
        
        Request Body - **JSON**
        Parameter | Type     | Description                |
        | :-------- | :------- | :------------------------- |
        | `popularity` | `string` | **Required**. popularity score |
        | `director` | `string` | **Required**. Directors name |
        | `genre` | `list` | **Required**. Genre |
        | `imdb_score` | `string` | **Required**. imdb score |
        | `name` | `string` | **Required**. Movie name |

    - Delete Movie

        ```http
        DELETE https://imdb-fynd-in.herokuapp.com/v1/imdb/movies/{movie_id}
        ```

    - View/Search Movies

        ```http
        GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies
        ```

- User
    - View/Search Movies

        ```http
        GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies
        ```

## Movie Search Guide
- Search by `movie or directors` name

    ```http
    GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?search=batman
    ```

    ```http
    GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?search=christopher%20nolan
    ```

- Filter by `genre`

    ```http
    GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?genre=action`
    ```

    ```http
    GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?genre=thriller
    ```

    ```http
    GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?genre=action,thriller
    ```

- Filter by `popularity` range
    - Filter movies which has popularity between 0 to 50

        ```http
        GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?p_srange=0&p_erange=50
        ```

    - Filter movies which has popularity between 50 to 100

        ```http
        GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?p_srange=50&p_erange=100
        ```

- Filter by `IMDB score` range
    - Filter movies which has IMDB score between 0 to 5

        ```http
        GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?s_srange=0&s_erange=5
        ```
    - Filter movies which has IMDB score between 5 to 10

        ```http
        GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?s_srange=5&s_erange=10
        ```

- Filter with `popularity and IMDB score` range
    - Filter movies which has IMDB score between 0 to 5 and popularity between 0 to 50

        ```http
        GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?s_srange=0&s_erange=5&p_srange=0&p_erange=50
        ```

- Sorting and order
    - Sort by `popularity score` - `Ascending`

        ```http
        GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?sortby=popularity&orderby=asc
        ```

    - Sort by `popularity score` - `Descending`

        ```http
        GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?sortby=popularity5&orderby=desc
        ```

    - Sort by `IMDB score` - `Ascending`

        ```http
        GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?sortby=imdb_score&orderby=asc
        ```
    - Sort by `IMDB score` - `Descending`

        ```http
        GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?sortby=imdb_score&orderby=desc
        ```

    - Change default ordering

        ```http 
        GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?orderby=desc
        ```

    - `If sorting and ordering params not passed then by default documents will be sorted in ascending order with ObjectId field`

- Limit

    ```http
    GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?limit=10
    ```

- offset

    ```http
    GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?offset=10&limit=10
    ```
    
- Search and filter with everything

    ```http
    GET https://imdb-fynd-in.herokuapp.com/v1/imdb/movies?search=batman&genre=action&p_srange=0&p_erange=80&s_srange=0&s_erange=10&sortby=imdb_score&orderby=desc&limit=10
    ```

    - Feel free to try different filters
