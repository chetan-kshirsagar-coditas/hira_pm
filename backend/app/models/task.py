from sqlalchemy import Column, ForeignKey, DateTime, func, String, Text, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.core.database.db import Base
import uuid
from app.enum.task_state import TaskState

class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.organization_id"), nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.project_id"), nullable=False)
    task_title = Column(String, nullable=False)
    task_description = Column(Text, nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    created_at = Column(DateTime, default=func.now())
    estimated_deadline = Column(DateTime, nullable=False)
    modified_at = Column(DateTime, server_default=func.now())
    state = Column(Enum(TaskState), nullable=False)
