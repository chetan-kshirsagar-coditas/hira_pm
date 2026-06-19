from app.core.database.db import Base
from sqlalchemy import Column, ForeignKey, Text, Enum, func, DateTime, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.enum.project_type import ProjectType

class Project(Base):
    __tablename__ = "projects"

    project_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.organization_id"), nullable=False)
    project_name = Column(String, nullable=False)
    project_description = Column(Text, nullable=False)
    project_type = Column(Enum(ProjectType), nullable=False)
    created_at = Column(DateTime, default=func.now())
    is_deleted = Column(Boolean, default=False)