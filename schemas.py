from typing import List, Optional
from pydantic import BaseModel

# Requirement Table
class RequirementBase(BaseModel):
    description:str 
    attribute_id:int

class RequirementCreate(RequirementBase):
    pass

class Requirement(RequirementBase):
    id: int
    class Config:
        orm_mode = True

class AttributeTemplateBase(BaseModel):
    name: str
    slug: str
    description: str

class AttributeTemplateCreate(AttributeTemplateBase):
    pass

class AttributeTemplate(AttributeTemplateBase):
    id: int
    class Config:
        orm_mode = True

# Attribute Table
class AttributeBase(BaseModel):
    template_id: int
    project_id: int

class AttributeCreate(AttributeBase):
    pass

class Attribute(AttributeBase):
    id: int
    prioridad: Optional[int] = 0
    requirements:List[Requirement]=[]
    template: AttributeTemplate
    class Config:
        orm_mode = True

# ARCHITECTURAL PATTERN
class ArchitecturePatternBase(BaseModel):
    title: str
    description: Optional[str] = None
    

class ArchitecturePatternCreate(ArchitecturePatternBase):
    pass

class ArchitecturePattern(ArchitecturePatternBase):
    id: int
    #team: List[User] = []
    attributes: List[Attribute] = [] 
    class Config:
        orm_mode = True

# PROJECT TABLE
class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    #team: List[User] = []
    architecture_pattern: Optional[ArchitecturePattern] 
    architecture_pattern_id: Optional[int]
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
        