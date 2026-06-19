import jwt
from cryptography.hazmat.primitives import serialization
from app.core.config.config import settings


class JWTHelper:

    @staticmethod
    def load_key(key_url: str, key_type: str):
        if key_type == 'public':
            with open(key_url, 'rb') as f:
                return serialization.load_pem_public_key(
                    f.read(),
                )
        elif key_type == 'private':
            with open(settings.PRIVATE_KEY_PATH, 'rb') as f:
                return serialization.load_pem_private_key(
                    f.read(),
                    password=None
                )
        else:
            return None
        

    @staticmethod
    def generate_jwt(payload: dict):    
        return {"access_token" : jwt.encode(payload, key=JWTHelper.load_key(settings.PRIVATE_KEY_PATH, 'private'), algorithm=settings.ALGORITHM),
                "token_type" : "bearer"}

    @staticmethod
    def decode_jwt(jwt_string: str):
        return jwt.decode(jwt_string, key=JWTHelper.load_key('public_key.pem', 'public'), algorithms=[settings.ALGORITHM])
