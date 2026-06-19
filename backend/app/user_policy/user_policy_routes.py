from fastapi import APIRouter, Depends
from app.core.database.db import db_helper
from sqlalchemy.orm import Session
from app.user_policy.user_policy_schema import PolicyGrant, PolicyRevoke
from app.user_policy.user_policy_service import UserPolicyService as permission_service
from app.models.users import User
from app.utils.role_checker.role_checker import RoleChecker
import uuid


router = APIRouter(prefix="/permissions", tags=["permissions"])

@router.post("/grant")
def grant_permission(payload: PolicyGrant, db: Session = Depends(db_helper.get_db), user: User = Depends(RoleChecker.required_policies(["ORGADMIN", "SUPERADMIN"]))):
    return permission_service.grant_policy_to_user(payload.policy_id, payload.user_id, db)

@router.post("/revoke")
def revoke_permission(payload: PolicyRevoke, db: Session = Depends(db_helper.get_db), user: User = Depends(RoleChecker.required_policies(["ORGADMIN", "SUPERADMIN"]))):
    return permission_service.revoke_policy_for_user(payload.policy_id, payload.user_id, db)

@router.get("/get/{user_id}")
def get_user_permissions(user_id: uuid.UUID, db: Session = Depends(db_helper.get_db), user: User = Depends(RoleChecker.required_policies(["ORGADMIN", "SUPERADMIN"]))):
    return permission_service.get_policies_for_user(user_id, db)