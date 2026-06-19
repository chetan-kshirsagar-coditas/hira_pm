import uuid
from app.models.project import Project
from app.projects.project_repository import ProjectRepository as project_repository
from sqlalchemy.orm import Session
from app.roles.role_service import RoleService as role_service
from app.models.users import User
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException
from app.organization.organization_service import OrganizationService as organization_service


class ProjectService:
    
    @staticmethod
    def create_new_project(organization_id: uuid.UUID, project_name: str, project_description: str, project_type: str, db: Session, user: User):
        
        new_project = Project(
            organization_id=organization_id,
            project_name=project_name, 
            project_description=project_description,
            project_type=project_type,
        )
        created_project = project_repository.create_new_project(new_project, db)
        
        # upon creation of a new project create default project roles: priject owner and project collaborator
        owner_role = role_service.create_role(
            organization_id = user.organization_id,
            role_name="Owner",
            project_id = created_project.project_id,
            created_by=user.user_id,
            role_type="SYSTEM",
            db=db
            )
        collaborator_role = role_service.create_role(
            organization_id = user.organization_id,
            role_name="Collaborator",
            project_id = created_project.project_id,
            created_by=user.user_id,
            role_type="SYSTEM",
            db=db
            )
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": f"New project {project_name} created successfully"
            }
        )


    @staticmethod
    def get_projects_by_organization_id(organization_id: uuid.UUID, db: Session):
        is_organization_deleted = organization_service.get_organization_by_organization_id(organization_id, db).is_deleted
        if is_organization_deleted:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organization is archived"
            )
        return project_repository.get_projects_by_organization_id(organization_id, db)
    

    @staticmethod
    def get_project_by_project_id(project_id: uuid.UUID, db: Session):
        project = project_repository.get_project_by_project_id(project_id, db)
        is_organization_deleted = organization_service.get_organization_by_organization_id(project.organization_id, db).is_deleted
        if is_organization_deleted:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organization is deleted"
            )
        return project
    

    @staticmethod
    def update_project(project_id: uuid.UUID, new_project_name: str | None, new_description: str|None, new_project_type: str| None, db: Session):
        existing_project = ProjectService.get_project_by_project_id(project_id, db)
        if not existing_project:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail="project not found"
            )
        is_organization_deleted = organization_service.get_organization_by_organization_id(existing_project.organization_id, db).is_deleted
        if is_organization_deleted:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organization is deleted"
            )
        if new_project_name:
            existing_project.project_name = new_project_name
        if new_description:
            existing_project.project_description = new_description
        if new_project_type:
            existing_project.project_type = new_project_type
        db.commit()
        db.refresh(existing_project)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Project updated successfully."
            }
        )

    @staticmethod
    def delete_project(project_id: uuid.UUID, db: Session):
        existing_project = ProjectService.get_project_by_project_id(project_id, db)
        is_organization_deleted = organization_service.get_organization_by_organization_id(existing_project.organization_id, db).is_deleted
        if is_organization_deleted:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organization is deleted"
            )
        if not existing_project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )
        return project_repository.archive_project(existing_project, db)
    
    @staticmethod
    def restore_project(project_id: uuid.UUID, db: Session):
        existing_project = ProjectService.get_project_by_project_id(project_id, db)
        is_organization_deleted = organization_service.get_organization_by_organization_id(existing_project.organization_id, db).is_deleted
        if is_organization_deleted:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organization is deleted"
            )
        if not existing_project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )
        return project_repository.unarchive_project(existing_project, db)


    @staticmethod
    def get_active_projects(organization_id: uuid.UUID, db: Session):
        is_organization_deleted = organization_service.get_organization_by_organization_id(organization_id, db).is_deleted
        if is_organization_deleted:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organization is deleted"
            )
        active_projects = project_repository.get_active_projects(organization_id, db)
        return active_projects