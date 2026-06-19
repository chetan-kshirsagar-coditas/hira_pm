from sqlalchemy import Column, ForeignKey, DateTime, func, Text
from sqlalchemy.dialects.postgresql import UUID
from app.core.database.db import Base
import uuid

class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.organization_id"), nullable=False)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.task_id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())