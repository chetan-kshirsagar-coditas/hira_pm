from sqlalchemy.orm import Session
from app.users.user_service import UserService as user_service
from app.utils.otp_service.otp_handler import OTPHandler
from fastapi import HTTPException, status
from app.user_policy.user_policy_service import UserPolicyService as user_policy_service
from app.utils.jwt_auth.jwt_helper import JWTHelper
from app.models.users import User
from fastapi.responses import JSONResponse
from app.utils.passwords.password_helper import PasswordHelper
from app.utils.redis_handle.redis_client import RedisClient
from app.organization.organization_service import OrganizationService as organization_service
from app.user_policy.user_policy_service import UserPolicyService as user_policy_service
import uuid

from app.utils.passwords.password_helper import PasswordHelper as password_helper

class LoginService:
    @staticmethod
    def login(email: str, db: Session):
        existing_user = user_service.get_user_by_email(email, db)
        if not existing_user:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "message": "OTP Sent Successfully"
                }
            )
        else:
            return OTPHandler.generate_otp(email)
        
    @staticmethod
    def verify_otp(email: str, user_input_otp: int, db: Session):
        user = OTPHandler.verify_otp(email, str(user_input_otp), db)
        if not isinstance(user, User):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid OTP"
            )
        if not user:
            raise HTTPException(
                detail="User not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        user_policies = user_policy_service.get_policies_for_user(user.user_id, db)
        
        payload = {
            "name": user.name,
            "email": email,
            "policies":user_policies,                      
        }
        return JWTHelper.generate_jwt(payload)
        
    

    @staticmethod
    def org_admin_set_password(token: str, email: str, password: str, db: Session):
        hashed_token = token
        raw_token = str(tok := RedisClient.client().get(email))[2:-1]
        if tok == None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password set link expired"
            )
        print(tok)
        is_verified = PasswordHelper.verify_otp(hashed_token, raw_token)
        # verify otp function compares hashvalue to user input.
        if not is_verified:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="something went wrong"
            )
        payload  = JWTHelper.decode_jwt(raw_token)
        existing_organization = organization_service.get_org_by_admin_email(payload["org_admin_email"], db)
        if existing_organization.is_active == True:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="User already has password set."
            )
        new_user = User(
            organization_id = payload['organization_id'],
            email = payload['org_admin_email'],
            name = payload['org_admin_name'],
            hashed_password = PasswordHelper.hash_password(password)
        )
        created_user = user_service.create_new_user(new_user, db)
        organization = organization_service.get_org_by_admin_email(email, db)
        organization.is_active=True
        
        db.commit()
        db.refresh(organization)
        user_policy_service.grant_policy_to_user(created_user.user_id, uuid.UUID("51c130af-66ba-4ed6-8409-e6bd029cef96"), db)
        RedisClient.client().delete(email)

        return JSONResponse(
            content={
                "message": "User created Successfully",
            },
            status_code = status.HTTP_201_CREATED
        )
    
    @staticmethod
    def get_token(email: str, password: str, db: Session):
        user = user_service.get_user_by_email(email, db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        is_verified = password_helper.verify_otp(user.hashed_password, password)
        if is_verified:
            
            user_policies = user_policy_service.get_policies_for_user(user.user_id, db)
        
            payload = {
                "name": user.name,
                "email": email,
                "policies":user_policies,                      
            }
            
            return JWTHelper.generate_jwt(payload)
        else:
            return JSONResponse(
                status_code = status.HTTP_400_BAD_REQUEST,
                content={
                    "message": "Invalid password"
                }
            )
            