from pydantic import BaseModel, Field
import uuid

class ProjectCreate(BaseModel):
    project_name: str = Field(..., min_length=3)
    project_description: str = Field(..., min_length=1)
    project_type: str = Field(...)

class ProjectModify(BaseModel):
    new_project_name: str | None = None
    new_project_description: str | None = None 
    new_project_type: str | None = None