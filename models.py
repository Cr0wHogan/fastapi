from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

project_user_table = Table('association', Base.metadata,
    Column('users_id', Integer, ForeignKey('users.id')),
    Column('projects_id', Integer, ForeignKey('projects.id'))
)

class AttributeTemplate(Base):
    __tablename__ = "attributes_templates" 
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String) 
    description= Column(String) 

class Attribute(Base):
    __tablename__ = "attributes" 
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    template_id = Column(Integer, ForeignKey("attributes_templates.id"))
    prioridad = Column(Integer)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    #hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
   
    projects = relationship("Project", secondary=project_user_table)

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    #team = relationship("User", secondary=project_user_table)
    attributes = relationship("Attribute", backref="projects") 