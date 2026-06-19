from app.core.database.db import Base
from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(Base):
    __tablename__ = "users"
    
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.organization_id"), nullable=True)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

