from app.core.database.db import Base
from sqlalchemy import Column, String, ForeignKey, Text, Enum, func, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.enum.role_type import RoleType

class Role(Base):
    __tablename__ = "roles"

    role_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.organization_id"), nullable=True)
    role_name = Column(String, nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.project_id"), nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    role_type = Column(Enum(RoleType), nullable=False)
    