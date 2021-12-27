from typing import List, Optional

from pydantic import BaseModel


class ProjectBase(BaseModel):
    title: str


class ProjectCreate(ProjectBase):
    user_id: int


class ProjectUpdate(ProjectBase):
    title: Optional[str] = None

class Project(ProjectBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True
