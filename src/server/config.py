import os
import sys

JWT_SECRET = os.environ.get("JWT_SECRET", "secret")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS256")
if None in (JWT_SECRET, JWT_ALGORITHM):
    sys.exit(1)

MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "ovhHQERSZAKlQTEb")
if not MONGO_PASSWORD:
    sys.exit(1)