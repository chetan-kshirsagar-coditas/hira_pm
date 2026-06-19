from pydantic import BaseModel, EmailStr, Field
from app.enum.subscription_type import SubscriptionType
import uuid


class OrganizationCreate(BaseModel):
    organization_name: str
    org_admin_name: str
    org_admin_email: EmailStr
    subscription_name: str

class OrganizationModify(BaseModel):
    organization_name: str | None = None
    org_admin_name: str | None = None
    subscription_name: str | None = None


class OrganizationDelete(BaseModel):
    organization_id: uuid.UUID = Field(...)