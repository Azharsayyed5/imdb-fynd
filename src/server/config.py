import os
import sys

JWT_SECRET = os.environ.get("JWT_SECRET", "secret")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS256")
if None in (JWT_SECRET, JWT_ALGORITHM):
    sys.exit(1)

MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "ovhHQERSZAKlQTEb")
MONGO_HOST = os.environ.get("MONGO_HOST", "cluster0.vgoq0.mongodb.net")
MONGO_USER = os.environ.get("MONGO_USER", "root")
MONG_DATABASE = os.environ.get("MONG_DATABASE", "myFirstDatabase")
if None in (MONGO_PASSWORD, MONGO_HOST, MONGO_HOST, MONG_DATABASE):
    sys.exit(1)

EXCEPTION_RESPONSE = "Something went wrong! Report issue"