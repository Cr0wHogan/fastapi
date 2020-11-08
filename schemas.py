from typing import List, Optional
from pydantic import BaseModel

# Requeriment Table
class RequerimentBase(BaseModel):
    name:str 
    attribute_id:int
    class Config:
        orm_mode = True

class RequerimentCreate(RequerimentBase):
    pass

class Requeriment(RequerimentBase):
    id: int
    class Config:
        orm_mode = True

class AttributeTemplateBase(BaseModel):
    name: str
    description: str

class AttributeTemplateCreate(AttributeTemplateBase):
    pass

class AttributeTemplate(AttributeTemplateBase):
    id: int
    class Config:
        orm_mode = True

# Attribute Table
class AttributeBase(BaseModel):
    prioridad: int

class AttributeCreate(AttributeBase):
    pass

class Attribute(AttributeBase):
    id: int
    template_id: int
    project_id: int
    requeriments:List[Requeriment]=[]
    class Config:
        orm_mode = True

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
    attributes: List[Attribute] = [] 
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
        