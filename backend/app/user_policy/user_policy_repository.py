from sqlalchemy.orm import Session
from app.models.user_policy import UserPolicy
import uuid
from sqlalchemy import select, and_
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from app.models.policy import Policy

class UserPolicyRepository:


    @staticmethod
    def get_user_policy_record(user_id: uuid.UUID, policy_id: uuid.UUID, db: Session):
        return db.execute(select(UserPolicy).where(and_(UserPolicy.user_id == user_id, UserPolicy.policy_id == policy_id))).scalars().first()


    @staticmethod
    def grant_policy_to_user(user_policy_record: UserPolicy, db: Session):
        try:
            db.add(user_policy_record)
            db.commit()
            db.refresh(user_policy_record)
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Database Error occured while granting user policy. {e}"
            )
        return user_policy_record
    
    @staticmethod
    def revoke_policy_for_user(user_id: uuid.UUID, policy_id: uuid.UUID, db: Session):
        user_policy_record = db.execute(select(UserPolicy).where(and_(UserPolicy.user_id == user_id, UserPolicy.policy_id == policy_id))).scalars().first()
        db.delete(user_policy_record)
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'message': 'Permission Revoked Successfully!'
            }
        )
    

    @staticmethod
    def get_user_policies(user_id: uuid.UUID, db: Session):
        policy_ids = db.execute(select(UserPolicy.policy_id).where(UserPolicy.user_id == user_id)).scalars().all()
        policies = db.execute(select(Policy.policy_name).where(Policy.policy_id.in_(policy_ids))).scalars().all()
        return policies