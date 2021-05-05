from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handler import decodeJWT


class JWTBearer(HTTPBearer):

    """A handler class to verify the authenticity of the authorization header
    """
    
    def __init__(self, auto_error: bool = True):
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
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
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