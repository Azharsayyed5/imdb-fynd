import sys
import os
import time
from typing import Dict
import jwt
from decouple import config
from pathlib import Path
sys.path.append(os.path.dirname(Path(os.path.abspath(__file__)).parent.parent))
from server.config import JWT_ALGORITHM, JWT_SECRET


def token_response(token: str):

    """To return access token

    Returns:
        Dict: Access token
    """

    return {"access_token": token}


def signJWT(user_id: str, role: str):

    """
    Singing the new JWT token and assigning it to user with payload containing
    user_id and role

    Args:
    user_id (str): User_id
    role (str): user role

    Returns:
        function: Calls another function which retuns the JWT token

    """

    payload = {
        "user_id": user_id,
        "role": role,
        "expires": time.time() + 3600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str):

    """Decoding JWT TOken with the hlp of secret key and hashing algorithm

    Args:
        token (str): Auth token to be decoded

    Returns:
        dict: Payload
    """
    
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
