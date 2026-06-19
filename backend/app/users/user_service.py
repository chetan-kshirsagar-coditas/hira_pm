from sqlalchemy.orm import Session
from app.users.user_repository import UserRepository as user_repository
from fastapi.responses import JSONResponse
from fastapi import status
from app.models.users import User
from app.users.user_schema import UserResponse


class UserService:

    @staticmethod
    def get_user_by_email(email: str, db: Session) -> UserResponse:
        user = user_repository.get_user_by_email(email, db)
        if not user:
            return None
        return user
    
    @staticmethod
    def create_new_user(new_user: User, db: Session):
        return user_repository.create_new_user(new_user, db)