from fastapi import HTTPException, Request
from typing import List
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handler import decodeJWT

class RoleChecker(HTTPBearer):

    """Permission Handler Class
    """

    def __init__(self, allowed_roles: List, auto_error: bool = True):
        self.allowed_roles = allowed_roles
        super(RoleChecker, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):

        """Gets called upon initialization of the class, The function gets the auth header
        and verifies it and after verification it checks if role in the payload is permissible

        Raises:
            HTTPException: `STATUS 403`, Operation not permitted
        """

        credentials: HTTPAuthorizationCredentials = await super(RoleChecker, self).__call__(request)
        if credentials:
            payload = self.verify_jwt(credentials.credentials)
            if payload['role'] not in self.allowed_roles:
                print(f"User {payload['user_id']} with role {payload['role']} not in {self.allowed_roles}")
                raise HTTPException(status_code=403, detail="Operation not permitted")

    def verify_jwt(self, jwtoken: str):

        """To verify and return the header payload

        Returns:
            dict: Header payload
        """

        try:
            print(jwtoken)
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        return payload