from app.models.role import Role
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError


class RoleRepository:

    @staticmethod
    def create_role(new_role: Role, db: Session):
        try:
            db.add(new_role)
            db.commit()
            db.refresh(new_role)
            return new_role
        except SQLAlchemyError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Database Error occured while creating new role"
            )