from sqlalchemy.orm import Session
from app.models.project import Project
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from fastapi.responses import JSONResponse
import uuid
from sqlalchemy import select, and_


class ProjectRepository:
    
    @staticmethod
    def create_new_project(new_project: Project, db: Session):
        try:
            db.add(new_project)
            db.commit()
            db.refresh(new_project)
            return new_project
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Database Error occured while creating new project\nMore details: {e}"
            )
        
    @staticmethod
    def archive_project(project: Project, db: Session):
        if project.is_deleted == True:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="project is already deleted"
            )
        project.is_deleted = True
        db.commit()
        db.refresh(project)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "project archived successfully"
            }
        )
    
    @staticmethod
    def get_project_by_project_id(project_id: uuid.UUID, db: Session):
        project = db.execute(select(Project).where(Project.project_id == project_id)).scalars().first()
        return project
    
    @staticmethod
    def get_projects_by_organization_id(organization_id: uuid.UUID, db: Session):
        projects = db.execute(select(Project).where(Project.organization_id == organization_id)).scalars().all()
        return projects
    

    @staticmethod
    def get_active_projects(organization_id: uuid.UUID, db: Session):
        return db.execute(select(Project).where(and_(Project.organization_id == organization_id, Project.is_deleted == False))).scalars().all()
    

    @staticmethod
    def unarchive_project(project: Project, db: Session):
        if project.is_deleted == False:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Project is already un-archived"
            )
        project.is_deleted= False
        db.commit()
        db.refresh(project)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'message': "Project un-archived successfully"
            }
        )