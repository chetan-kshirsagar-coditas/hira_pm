from app.utils.jwt_auth.jwt_helper import JWTHelper
from app.users.user_service import UserService as user_service
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from app.models.users import User
from app.core.database.db import db_helper
from app.user_policy.user_policy_service import UserPolicyService as user_policy_service



OAuth2Scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

class RoleChecker:

    @staticmethod
    def get_current_user(token: str =  Depends(OAuth2Scheme), db: Session = Depends(db_helper.get_db)):
        decoded_payload = JWTHelper.decode_jwt(token)
        email = decoded_payload.get("email")
        user = user_service.get_user_by_email(email, db)

        if not user:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="You are unauthorised"
            )
        return user
    

    @staticmethod
    def required_policies(permissions: list[str]):
        def checker(user: User = Depends(RoleChecker.get_current_user), db: Session = Depends(db_helper.get_db)):
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail="User Not found"
                )
            user_permissions = user_policy_service.get_policies_for_user(user.user_id, db)

            for permission in permissions:
                if permission not in user_permissions:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED, 
                        detail="You don't have permission to access this"
                    )
            return user
        return checker