from sqlalchemy import Column, String, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from app.core.database.db import Base
import uuid

class Attachment(Base):
    __tablename__ = "attachments"

    document_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.organization_id"), nullable=False)
    document_ref = Column(String, nullable=False)
    added_by = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    added_at = Column(DateTime, default=func.now())