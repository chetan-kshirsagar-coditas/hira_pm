from pydantic import BaseModel, EmailStr, Field


class OTPRequest(BaseModel):
    email: EmailStr

class OTPVerificationRequest(BaseModel):
    email: EmailStr
    entered_otp: int

class SetPassword(BaseModel):
    token: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8, max_length=30)

class LoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8, max_length=30)