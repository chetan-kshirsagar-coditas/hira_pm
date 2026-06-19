from sqlalchemy.orm import Session
from app.organization.organization_schema import OrganizationCreate
from app.models.organization import Organization
from app.organization.organization_repository import OrganizationRepository as organization_repository
from app.utils.passwords.password_helper import PasswordHelper
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException
import uuid

class OrganizationService:

    @staticmethod
    def create_organization(organization : OrganizationCreate, db: Session):
        organization_domain_name_ = organization.org_admin_email.split('@')[-1]
        existing_organization = organization_repository.get_organization_by_admin_email(organization.org_admin_email, db)
        if existing_organization:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail=f"Organization already exists"
            )
        second_check_org = organization_repository.get_organization_by_domain(organization_domain_name_, db)
        if second_check_org:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organization with the same domain name already exists"
        )
        new_organization_record = Organization(
            organization_name=organization.organization_name,
            organization_domain_name=organization_domain_name_,
            org_admin_name=organization.org_admin_name.title(),
            org_admin_email=organization.org_admin_email,
            subscription_name=organization.subscription_name,
        )
        try:
            new_organization = organization_repository.create_organization(new_organization_record, db)
            PasswordHelper.generate_set_password_link(organization.org_admin_email, db)
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error while creating new organization. {e}"
            )
        return JSONResponse(
            status_code = status.HTTP_201_CREATED,
            content={
                "message": "organization created successfully. Email sent to org admin."
            }
        )
    

    @staticmethod
    def get_org_by_admin_email(org_admin_email: str, db: Session):
        org = organization_repository.get_organization_by_admin_email(org_admin_email, db)
        if not org:
            return None
        return org


    @staticmethod
    def get_archived_organizations(db: Session):
        organizations = organization_repository.get_archived_organizations(db)
        return organizations


    @staticmethod
    def get_all_organizations(db: Session):
        organizations = organization_repository.get_all_organizations(db)
        return organizations
    

    @staticmethod
    def update_organization_details(
        organization_id: uuid.UUID, 
        organization_name: str | None, 
        organization_admin_name: str | None, 
        subscription_name: str | None, 
        db: Session,
        ):
        existing_organization = organization_repository.get_organization_by_id(organization_id, db)
        if not existing_organization:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail= "Organization not found"
            )
        return organization_repository.update_organization_details(existing_organization, organization_name, organization_admin_name, subscription_name, db)
    

    @staticmethod
    def archive_organization(organization_id: uuid.UUID, db: Session):
        existing_organization = organization_repository.get_organization_by_id(organization_id, db)
        if not existing_organization:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail="Couldn't find organization"
            )
        return organization_repository.archive_organization(existing_organization, db)
    

    @staticmethod
    def restore_organization(organization_id: uuid.UUID, db: Session):
        existing_organization = organization_repository.get_organization_by_id(organization_id, db)
        if not existing_organization:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail="Couldn't find organization"
            )
        return organization_repository.restore_organization(existing_organization, db)
    
    
    @staticmethod
    def get_organization_by_organization_id(org_id: uuid.UUID, db: Session):
        organization = organization_repository.get_organization_by_id(org_id, db)
        if not organization:
            return None
        return organization