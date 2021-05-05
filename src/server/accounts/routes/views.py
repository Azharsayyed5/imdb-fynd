import sys
import os
from pathlib import Path
sys.path.append(os.path.dirname(Path(os.path.abspath(__file__)).parent.parent.parent))
from fastapi import APIRouter, Body, Request, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
import datetime
from server.accounts.models.schema import (
    ErrorResponseModel, ResponseModel, UserSchema, UserLoginSchema, Token, GenericResponse
)
from server.accounts.models.database import (
    fetch_document, create_document, fetch_documents_all
)
from server.accounts.utils.utils import (
    verify_password
)
from server.auth.auth_handler import signJWT, decodeJWT
from server.auth.auth_bearer import JWTBearer
from server.config import EXCEPTION_RESPONSE

router = APIRouter()
Auth_handler = JWTBearer([])

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_description="Authorization Token", response_model=Token)
async def signup(user_data: UserSchema):

    """API endpoint for `registering new users in system`, first check if user already exists in database
    if already exists then send error response else successfully insert the user in database and generate
    new access token for the newly registered user with expirty of 1 hour.

    Args:
        `user_data` (UserSchema): singup pydantic schema

    Raises:
        HTTPException: `STATUS 409`, If user already exists in database
        HTTPException: `STATUS 500`, If any general exception occurs

    Returns:
        HTTPResponse: `STATUS 201 CREATED` for successful registration of user, else failure reponse
    """

    try:
        # Check if email address already exists in database
        user = await fetch_document({'email': user_data.email})
        if user:
            raise HTTPException(status_code=409, detail="User already registered.", headers={"X-Error": "User already registered in database"})
        # Create user
        signedup_user = await create_document(user_data)
        # Generate JWT Access token
        return signJWT(signedup_user['user_id'], signedup_user['role'])
    except Exception as GeneralException:
        print(f"Signup API - {GeneralException}")
        raise HTTPException(status_code=500, detail=EXCEPTION_RESPONSE, headers={"X-Error": EXCEPTION_RESPONSE})


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
        HTTPException: `STATUS 500`, If any general exception occurs

    Returns:
        HTTPResponse: `STATUS 200`, Successfully logged in
    """

    try:
        user = await fetch_document({'email': UserData.email}, True)
        if not user:
            raise HTTPException(status_code=404, detail="User does not exist, please signup", headers={"X-Error": "User does not exist"})
        # Verify password
        if verify_password(UserData.password, user['hashed_password']):
            return signJWT(user['user_id'], user['role'])
        else:
            # Password Verification Failed
            raise HTTPException(status_code=403, detail="Wrong credentials provided.", headers={"X-Error": "Wrong credentials provided."})
    except Exception as GeneralException:
        print(f"Login API - {GeneralException}")
        raise HTTPException(status_code=500, detail=EXCEPTION_RESPONSE, headers={"X-Error": EXCEPTION_RESPONSE})


@router.get("/me", response_description="User Account discription", response_model=GenericResponse)
async def show_account(token: dict = Depends(Auth_handler)):

    """`Show account details` for each particular user

    Args:
        `user_id` (str): Current user user_id

    Raises:
        HTTPException: `STATUS 404`, If user does not exists in database
        HTTPException: `STATUS 500`, If any general exception occurs

    Returns:
        HTTPResponse: `STATUS 200` Success, with user details
    """

    try:
        # Get Payload from Auth token
        payload = decodeJWT(token)
        # Get user from database
        user = await fetch_document({'user_id': payload['user_id']})
        if not user:
            raise HTTPException(status_code=404, detail="User does not exist", headers={"X-Error": "User does not exist"})
        response = ResponseModel(user, "Successfull")
        return response
    except Exception as GeneralException:
        print(f"Account detail - {GeneralException}")
        raise HTTPException(status_code=500, detail=EXCEPTION_RESPONSE, headers={"X-Error": EXCEPTION_RESPONSE})
