import os
import sys

JWT_SECRET = os.environ.get("JWT_SECRET", None)
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", None)
if None in (JWT_SECRET, JWT_ALGORITHM):
    sys.exit(1)

MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", None)
MONGO_HOST = os.environ.get("MONGO_HOST", None)
MONGO_USER = os.environ.get("MONGO_USER", None)
MONG_DATABASE = os.environ.get("MONG_DATABASE", None)
if None in (MONGO_PASSWORD, MONGO_HOST, MONGO_HOST, MONG_DATABASE):
    sys.exit(1)

EXCEPTION_RESPONSE = "Something went wrong! Report issue"