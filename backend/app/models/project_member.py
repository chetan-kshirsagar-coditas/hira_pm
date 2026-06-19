from sqlalchemy import Column, ForeignKey, DateTime, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from app.core.database.db import Base
import uuid

class ProjectMember(Base):
    __tablename__ = "project_member"

    __table_args__ = (
        UniqueConstraint("project_id", "user_id", name="unique_member_per_project"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.organization_id"), nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.project_id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.role_id"), nullable=False)
    assigned_at = Column(DateTime, default=func.now())