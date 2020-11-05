from typing import List, Optional
from pydantic import BaseModel

# PROJECT TABLE
class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    #team: List[User] = []

    class Config:
        orm_mode = True

# USER TABLE
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    #password: str
    pass

class User(UserBase):
    id: int
    is_active: bool
    projects: List[Project] = []

    class Config:
        orm_mode = True
        