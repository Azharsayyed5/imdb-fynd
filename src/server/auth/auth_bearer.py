import sys
import os
from fastapi import Request, HTTPException
from typing import List
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pathlib import Path
sys.path.append(os.path.dirname(Path(os.path.abspath(__file__)).parent.parent.parent))
from server.auth.auth_handler import decodeJWT
from server.logger import logging_handler

logger = logging_handler()


class JWTBearer(HTTPBearer):

    """A handler class to verify the authenticity of the authorization header
    """
    
    def __init__(self, allowed_roles: List = [], auto_error: bool = True):
        self.allowed_roles = allowed_roles
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):

        """Gets called upon initialization of the class, The function gets the auth header and checks
        its authenticity.

        Raises:
            HTTPException: `STATUS 403`, Invalid authentication scheme.
            HTTPException: `STATUS 403`, Invalid token or expired token.
            HTTPException: `STATUS 403`, Invalid authorization code.
 
        """

        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                logger.error(f"Invalid authentication scheme.")
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")

            payload = self.verify_jwt(credentials.credentials)
            if not payload:
                logger.error(f"Invalid token or expired token")
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")

            if self.allowed_roles: 
                if payload['role'] not in self.allowed_roles:
                    logger.error(f"User {payload['user_id']} with role {payload['role']} not in {self.allowed_roles}")
                    raise HTTPException(status_code=403, detail="Operation not permitted")

            return credentials.credentials
        else:
            logger.error(f"Invalid authorization code.")
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str):

        """To verify and return the header payload

        Returns:
            dict: Header payload
        """

        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        return payload