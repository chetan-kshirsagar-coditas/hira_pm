from sqlalchemy import Column, ForeignKey, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.core.database.db import Base

class UserPolicy(Base):
    __tablename__ = "user_policy"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    policy_id = Column(UUID(as_uuid=True), ForeignKey("policies.policy_id"), nullable=False)
    assigned_at = Column(DateTime, default=func.now())