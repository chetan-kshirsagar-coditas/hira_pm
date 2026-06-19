from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.projects.project_schema import ProjectCreate
from app.core.database.db import db_helper
from app.projects.project_service import ProjectService as project_service
import uuid
from app.utils.role_checker.role_checker import RoleChecker
from app.models.users import User
from app.projects.project_schema import ProjectModify



router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/create")
def create_new_project(new_project: ProjectCreate, db: Session = Depends(db_helper.get_db), user : User = Depends(RoleChecker.required_policies(["ORGADMIN"]))):
    """
    create new project
    """
    return project_service.create_new_project(user.organization_id, new_project.project_name, new_project.project_description, new_project.project_type, db, user=user)

@router.get("/get/{project_id}")
def get_project_by_project_id(project_id: uuid.UUID, db: Session = Depends(db_helper.get_db), user : User = Depends(RoleChecker.required_policies(["ORGADMIN", "PROJECT_OWNER", "PROJECT_DEVELOPER", "PROJECT_COLLABORATOR", "VIEWER", "EDITOR"]))):
    """
    fetch project by project id
    """
    return project_service.get_project_by_project_id(project_id, db)

@router.get("/get_by_organization_id/{organization_id}")
def get_project_by_organization_id(organization_id: uuid.UUID, db: Session = Depends(db_helper.get_db), user : User = Depends(RoleChecker.required_policies(["ORGADMIN"]))):
    """
    fetch project details by organization id
    """
    return project_service.get_projects_by_organization_id(organization_id, db)

@router.get("/get_active_projects/{organization_id}")
def get_active_projects(organization_id: uuid.UUID, db: Session = Depends(db_helper.get_db), user : User = Depends(RoleChecker.required_policies(["ORGADMIN"]))):
    return project_service.get_active_projects(organization_id, db)

@router.patch("update_project/{project_id}")
def update_project(project_id: uuid.UUID, new_project_details: ProjectModify, db: Session = Depends(db_helper.get_db), user : User = Depends(RoleChecker.required_policies(["ORGADMIN"]))):
    return project_service.update_project(project_id, new_project_details.new_project_name, new_project_details.new_project_description, new_project_details.new_project_type, db)

@router.delete("/delete/{project_id}")
def delete_project(project_id: uuid.UUID, db: Session = Depends(db_helper.get_db), user : User = Depends(RoleChecker.required_policies(["ORGADMIN", "PROJECT_OWNER"]))):
    return project_service.delete_project(project_id, db)

@router.patch("/restore/{project_id}")
def restore_project(project_id: uuid.UUID, db: Session = Depends(db_helper.get_db), user : User = Depends(RoleChecker.required_policies(["ORGADMIN", "PROJECT_OWNER"]))):
    return project_service.restore_project(project_id, db)

