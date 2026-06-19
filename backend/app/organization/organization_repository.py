from sqlalchemy.orm import Session
from app.models.organization import Organization
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
import uuid
from sqlalchemy import select, and_
from fastapi.responses import JSONResponse


class OrganizationRepository:

    @staticmethod
    def create_organization(organization: Organization, db: Session):
        try:
            db.add(organization)
            db.commit()
            db.refresh(organization)
            return organization
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Database Error occured while creating new organization {e}"
            )
    
    
    @staticmethod
    def get_all_organizations(db: Session):
        """
        superadmin function
        """
        return db.execute(select(Organization).where(and_(Organization.is_deleted == False, Organization.is_active == True))).scalars().all()
    
    @staticmethod
    def get_organization_by_admin_email(org_admin_email: str, db: Session):
        return db.execute(select(Organization).where(Organization.org_admin_email == org_admin_email)).scalars().first()
    
    @staticmethod
    def get_organization_by_id(organization_id: uuid.UUID, db: Session):
        return db.execute(select(Organization).where(Organization.organization_id == organization_id)).scalars().first()
    
    @staticmethod
    def update_organization_details(existing_organization: Organization, organization_name: str, organization_admin_name: str, subscription_name: str, db: Session):
        if organization_name:
            existing_organization.organization_name = organization_name,
        if organization_admin_name:
            existing_organization.org_admin_name = organization_admin_name,
        if subscription_name:
            existing_organization.subscription_name = subscription_name
        db.commit()
        db.refresh(existing_organization)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "organization details updated successfully"
            }
        )
    
    @staticmethod
    def get_archived_organizations(db: Session):
        return db.execute(select(Organization).where(Organization.is_deleted == True)).scalars().all()

    @staticmethod
    def archive_organization(organization: Organization, db: Session):
        organization.is_deleted = True
        db.commit()
        db.refresh(organization)
        return JSONResponse(
            content={
                "message": "organization deleted successfully"
            },
            status_code=status.HTTP_200_OK
        )
    
    @staticmethod
    def restore_organization(organization: Organization, db: Session):
        organization.is_deleted = False
        db.commit()
        db.refresh(organization)
        return JSONResponse(
            content={
                "message": "organization Restored successfully"
            },
            status_code=status.HTTP_200_OK
        )
    
    @staticmethod
    def get_organization_by_domain(domain: str, db: Session):
        return db.execute(select(Organization).where(Organization.organization_domain_name == domain)).scalars().first()