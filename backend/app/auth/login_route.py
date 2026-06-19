from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.login_service import LoginService
from app.core.database.db import db_helper
from app.auth.login_schema import OTPRequest, OTPVerificationRequest
from app.auth.login_schema import SetPassword
from app.auth.login_schema import LoginSchema
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth", tags=["login"])


@router.post("/request_otp")
def request_otp(request: OTPRequest, db: Session = Depends(db_helper.get_db)):
    return LoginService.login(request.email, db)

@router.post("/verify_otp")
def verify_otp(verification_request: OTPVerificationRequest, db: Session = Depends(db_helper.get_db)):
    return LoginService.verify_otp(verification_request.email, verification_request.entered_otp, db)


@router.post("/org_admin_set_password")
def set_password(set_password_payload: SetPassword, db: Session = Depends(db_helper.get_db)):
    return LoginService.org_admin_set_password(set_password_payload.token, set_password_payload.email, set_password_payload.password, db)

@router.post("/token")
def login(login_creds: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db_helper.get_db)):
    return LoginService.get_token(login_creds.username, login_creds.password, db)