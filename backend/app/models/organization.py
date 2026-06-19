from sqlalchemy import Column, String, DateTime, func, Enum, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.core.database.db import Base
from app.enum.subscription_type import SubscriptionType
import uuid

class Organization(Base):
    __tablename__ = "organizations"

    organization_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_name = Column(String, nullable=False)
    organization_domain_name = Column(String, nullable=False)
    org_admin_name = Column(String, nullable=False)
    org_admin_email = Column(String, unique=True, nullable=False)
    subscription_name = Column(Enum(SubscriptionType), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
