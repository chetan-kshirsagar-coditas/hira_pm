from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException
import secrets
from datetime import datetime, timedelta
from app.utils.email.email_service import EmailService as email_service
from app.utils.redis_handle.redis_client import RedisClient
from app.organization.organization_repository import OrganizationRepository as organization_repo
from app.utils.jwt_auth.jwt_helper import JWTHelper



password_context = CryptContext(schemes="bcrypt", deprecated="auto")

class PasswordHelper:

    @staticmethod
    def hash_password(plain_password: str):
        return password_context.hash(plain_password)
    
    @staticmethod
    def hash_otp(otp_code: str):
        return password_context.hash(otp_code)
    
    @staticmethod
    def verify_otp(otp_hash: str, user_input_otp: int):
        if password_context.verify(str(user_input_otp), str(otp_hash)):
            return True
        return False
    
    @staticmethod
    def generate_set_password_link(user_email: str, db: Session):
        existing_organization = organization_repo.get_organization_by_admin_email(user_email, db)
        encodable_payload = {
            "organization_id": str(existing_organization.organization_id),
            "org_admin_email": user_email,
            "org_admin_name": existing_organization.org_admin_name,
        }
        
        raw_token = JWTHelper.generate_jwt(encodable_payload)['access_token']
        hashed_token = PasswordHelper.hash_password(str(raw_token))

        try:
            RedisClient.client().set(user_email, raw_token, ex=86400)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Redis cache server error. {e}"
            )
        
        reset_link = f"http://localhost:5173/auth/org_admin_set_password?token={hashed_token}&email={user_email}"
        
        subject = "Team HIRA - Set Password Link"
        body= f"Your link for setting password is n {reset_link}"

        try:
            email_service.send_mail(user_email, subject, body)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Email service error {e}"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Invite link sent successfully."
            }
        )