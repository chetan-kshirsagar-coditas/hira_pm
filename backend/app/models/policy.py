from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from app.core.database.db import Base
import uuid

class Policy(Base):
    __tablename__ = "policies"

    policy_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    policy_name = Column(String, nullable=False)
    allowed_resource = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())