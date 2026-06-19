import uuid
from sqlalchemy.orm import Session
from app.models.role import Role
from app.roles.role_repository import RoleRepository as role_repository



class RoleService:

    @staticmethod
    def create_role(
        organization_id: uuid.UUID,
        role_name: str, 
        project_id: uuid.UUID, 
        created_by: uuid.UUID, 
        role_type: str, 
        db: Session
        ):
        new_role = Role(
            organization_id = organization_id,
            role_name=role_name,
            project_id = project_id,
            created_by=created_by,
            role_type = role_type,
        )
        return role_repository.create_role(new_role, db)
