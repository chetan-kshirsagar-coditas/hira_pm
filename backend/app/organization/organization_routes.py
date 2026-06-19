from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.organization.organization_service import OrganizationService as organization_service
from app.organization.organization_schema import OrganizationCreate
from app.core.database.db import db_helper
from app.organization.organization_schema import OrganizationModify, OrganizationDelete
import uuid
from app.utils.role_checker.role_checker import RoleChecker
from app.models.users import User


router = APIRouter(prefix="/organization", tags=["organization"])


@router.post("/create")
def create_new_organization(organization_payload: OrganizationCreate, db: Session = Depends(db_helper.get_db), user: User = Depends(RoleChecker.required_policies(["SUPERADMIN"]))):
    return organization_service.create_organization(organization_payload, db)


@router.patch("/update/{organization_id}")
def update_organization_details(organization_id: uuid.UUID, new_organization: OrganizationModify, db: Session = Depends(db_helper.get_db), user: User = Depends(RoleChecker.required_policies(["SUPERADMIN"]))):
    return organization_service.update_organization_details(organization_id, new_organization.organization_name, new_organization.org_admin_name, new_organization.subscription_name, db)

@router.get("/get_all_active_organizations")
def get_all_organizations(db: Session = Depends(db_helper.get_db), user: User = Depends(RoleChecker.required_policies(["SUPERADMIN"]))):
    return organization_service.get_all_organizations(db)


@router.get("/get_archived")
def get_archived_organizations(db: Session = Depends(db_helper.get_db), user: User = Depends(RoleChecker.required_policies(["SUPERADMIN"]))):
    return organization_service.get_archived_organizations(db)


@router.delete("/delete/{organization_id}")
def archive_organization(organization_id: uuid.UUID, db: Session = Depends(db_helper.get_db), user: User = Depends(RoleChecker.required_policies(["SUPERADMIN"]))):
    return organization_service.archive_organization(organization_id, db)


@router.patch("/restore/{organization_id}")
def restore_organization(organization_id: uuid.UUID, db: Session = Depends(db_helper.get_db), user: User = Depends(RoleChecker.required_policies(["SUPERADMIN"]))):
    return organization_service.restore_organization(organization_id, db)


@router.get("/get_organization_by_id/{organization_id}")
def get_organization_by_org_id(organization_id: uuid.UUID, db: Session = Depends(db_helper.get_db), user: User = Depends(RoleChecker.required_policies(["SUPERADMIN"]))):
    return organization_service.get_organization_by_organization_id(organization_id, db)