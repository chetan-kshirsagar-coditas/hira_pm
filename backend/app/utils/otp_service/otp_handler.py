import redis
import random
import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from app.utils.passwords.password_helper import PasswordHelper
from app.users.user_service import UserService as user_service
from app.utils.email.email_service import EmailService as email_service
from app.utils.redis_handle.redis_client import RedisClient



class OTPHandler:
    @staticmethod
    def generate_otp(email: str):
        """
        generates otp for a user (email)
        """
        hashed_otp = PasswordHelper.hash_otp(str(otp:=random.randint(1000,9999)))
        print(otp)
        try:
            RedisClient.client().set(email, hashed_otp, ex=180)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error in otp service {e}"
            )
        try:
            email_subject="Your HIRA Login OTP"
            email_body=f"Your OTP For logging into HIRA is {otp}.\nThis code is valid for 3 minutes."
            email_service.send_mail(email, email_subject, email_body)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    "message": "Email OTP service failed"
                }
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "OTP Sent successfully."
            }
        )
    
    @staticmethod
    def verify_otp(email: str, otp: str, db: Session):
        unprocessed_otp_hash=RedisClient.client().get(email)
        if not unprocessed_otp_hash:
            raise HTTPException(
                status_code=status.HTTP_408_REQUEST_TIMEOUT,
                detail="OTP Expired."
            )
        otp_hash = str(unprocessed_otp_hash)[2:-1]
        is_correct_otp = PasswordHelper.verify_otp(otp_hash=otp_hash, user_input_otp=otp)
        if is_correct_otp:
            return user_service.get_user_by_email(email, db)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'message': "Invalid OTP"
            }
        )