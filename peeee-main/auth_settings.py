import hashlib
from datetime import UTC, datetime, timedelta, timezone
from authx import AuthX, AuthXConfig
import bcrypt 
import os


SECRET_KEY = os.environ["qazxswokmnji"]

config = AuthXConfig(
    JWT_SECRET_KEY=SECRET_KEY,
    JWT_TOKEN_LOCATION=["cookies"],,
    JWT_ACCESS_COOKIE_NAME="access_token",
    JWT_REFRESH_COOKIE_NAME="refresh_token",
    JWT_ACCESS_TOKEN_EXPIRES=15,
    JWT_REFRESH_TOKEN_EXPIRES=60*24*7,
    JWT_COOKIE_CSRF_PROTECT=True,
    JWT_COOKIE_HTTP_ONLY=True,
    JWT_COOKIE_SECURE=False,
    JWT_COOKIE_SAMESITE="lax",
)

auth = AuthX(config=config)

