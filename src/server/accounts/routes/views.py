from fastapi import APIRouter, Body, Request, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
import datetime
from server.accounts.models.schema import (
    ErrorResponseModel, ResponseModel, UserSchema, UserLoginSchema, Token, Response
)
from server.accounts.models.database import (
    fetch_document, create_document, fetch_documents_all
)
from server.accounts.utils.utils import (
    verify_password
)
from server.auth.auth_handler import signJWT, decodeJWT
from server.auth.auth_bearer import JWTBearer

router = APIRouter()


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_description="Authorization Token", response_model=Token)
async def signup(user_data: UserSchema):

    """API endpoint for `registering new users in system`, first check if user already exists in database
    if already exists then send error response else successfully insert the user in database and generate
    new access token for the newly registered user with expirty of 1 hour.

    Args:
        `user_data` (UserSchema): singup pydantic schema

    Raises:
        HTTPException: `STATUS 409`, If user already exists in database

    Returns:
        HTTPResponse: `STATUS 201 CREATED` for successful registration of user, else failure reponse
    """

    user = await fetch_document({'email': user_data.email})
    if user:
        raise HTTPException(status_code=409, detail="User already registered.", headers={"X-Error": "User already registered in database"})
    signedup_user = await create_document(user_data)
    return signJWT(signedup_user['user_id'], signedup_user['role'])


@router.post("/login", response_description="Authorization Token", response_model=Token)
async def user_login(UserData: UserLoginSchema = Body(...)):

    """API endpoint for login, first check if user exists in database if exists then
    verify the plain password with previously hashed password stored in database.
    lastly generate JWT access token for the user with payload containing `user_id` and `role`

    Args:
        `UserData` (UserLoginSchema, optional): [description]. Defaults to Body(...).

    Raises:
        HTTPException: `STATUS 404`, If user does not exists in database
        HTTPException: `STATUS 403`, If user provided credentials are wrong

    Returns:
        HTTPResponse: `STATUS 200`, Successfully logged in
    """

    user = await fetch_document({'email': UserData.email}, True)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist, please signup", headers={"X-Error": "User does not exist"})
    if verify_password(UserData.password, user['hashed_password']):
        return signJWT(user['user_id'], user['role'])
    else:
        raise HTTPException(status_code=403, detail="Wrong credentials provided.", headers={"X-Error": "Wrong credentials provided."})


@router.get("/me", response_description="User Account discription", response_model=Response)
async def show_account(token: dict = Depends(JWTBearer())):

    """`Show account details` for each particular user

    Args:
        `user_id` (str): Current user user_id

    Raises:
        HTTPException: `STATUS 404`, If user does not exists in database

    Returns:
        HTTPResponse: `STATUS 200` Success, with user details
    """

    payload = decodeJWT(token)
    user = await fetch_document({'user_id': payload['user_id']})
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist", headers={"X-Error": "User does not exist"})
    response = ResponseModel(user, "Successfull")
    return response


@router.get("/list", dependencies=[Depends(JWTBearer())], response_description="List of registered users", response_model=Response)
async def show_users():

    """`Show all users` presently registered in system

    Returns:
        HTTPResponse: `STATUS 200` Success, List of registered users
    """

    users = await fetch_documents_all()
    print(users)
    response = ResponseModel(users, "Successfull")
    return response