from app.user_policy.user_policy_repository import UserPolicyRepository as user_policy_repository
from fastapi import HTTPException, status
from app.models.user_policy import UserPolicy
import uuid
from sqlalchemy.orm import Session


class UserPolicyService:
    
    @staticmethod
    def grant_policy_to_user(user_id: uuid.UUID, policy_id:uuid.UUID, db: Session):
        existing_user_policy_record = user_policy_repository.get_user_policy_record(user_id, policy_id, db)
        if existing_user_policy_record:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail=f"User already has this permission!"
            )
        new_user_policy_record = UserPolicy(
            user_id = user_id,
            policy_id = policy_id
        )
        return user_policy_repository.grant_policy_to_user(new_user_policy_record, db)

    @staticmethod
    def revoke_policy_for_user(user_id: uuid.UUID, policy_id: uuid.UUID, db: Session):
        existing_user_policy_record = user_policy_repository.get_user_policy_record(user_id, policy_id, db)
        if not existing_user_policy_record:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User does not have this permission. You can not revoke this permission."
            )
        return user_policy_repository.revoke_policy_for_user(user_id, policy_id, db)
    
    @staticmethod
    def get_policies_for_user(user_id: uuid.UUID, db: Session):
        return user_policy_repository.get_user_policies(user_id, db)