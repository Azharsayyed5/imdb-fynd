from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):

    """To verify password authentication

    Args:
        plain_password (str): Plain Password string
        hashed_password (str): Hashed Password string

    Returns:
        bool: Return boolean value upon checking whether both hashed and plain password are same
    """

    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):

    """Generate hashed password upon receiving a plain password

    Args:
        password (str): Plain password

    Returns:
        str: hashed password
    """

    return pwd_context.hash(password)