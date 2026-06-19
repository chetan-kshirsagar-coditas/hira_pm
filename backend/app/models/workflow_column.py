from sqlalchemy import Column, String, Integer, DateTime, func, ForeignKey
from app.core.database.db import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class WorkFlowColumn(Base):
    __tablename__ = "workflow_columns"
    
    column_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.organization_id"), nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.project_id"), nullable=False)
    column_title = Column(String, nullable=False)
    column_number = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())