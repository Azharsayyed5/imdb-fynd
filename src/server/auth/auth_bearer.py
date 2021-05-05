from fastapi import Request, HTTPException
from typing import List
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handler import decodeJWT


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
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")

            payload = self.verify_jwt(credentials.credentials)
            if not payload:
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")

            if self.allowed_roles: 
                if payload['role'] not in self.allowed_roles:
                    print(f"User {payload['user_id']} with role {payload['role']} not in {self.allowed_roles}")
                    raise HTTPException(status_code=403, detail="Operation not permitted")

            return credentials.credentials
        else:
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