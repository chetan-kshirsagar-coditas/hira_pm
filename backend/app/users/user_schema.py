from pydantic import BaseModel, EmailStr
import uuid


class UserResponse(BaseModel):
    user_id: uuid.UUID
    organization_id: uuid.UUID
    name: str
    email: EmailStr