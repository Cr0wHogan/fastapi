from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

project_user_table = Table('association', Base.metadata,
    Column('users_id', Integer, ForeignKey('users.id')),
    Column('projects_id', Integer, ForeignKey('projects.id'))
)

class Requirement(Base):
    __tablename__ = "requirements"
    id = Column(Integer, primary_key=True, index=True)
    attribute_id = Column(Integer, ForeignKey("attributes.id"))
    description = Column(String)

class AttributeTemplate(Base):
    __tablename__ = "attribute_templates" 
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String)
    slug = Column(String,unique=True,index=True)
    description= Column(String)

class Attribute(Base):
    __tablename__ = "attributes" 
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    template_id = Column(Integer, ForeignKey("attribute_templates.id"))
    prioridad = Column(Integer)

    requirements = relationship("Requirement", backref="attributes")
    template = relationship('AttributeTemplate', foreign_keys='Attribute.template_id')


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
    title = Column(String)  #Pensamos que puede ser unique en un futuro.
    description = Column(String)
    #team = relationship("User", secondary=project_user_table)
    attributes = relationship("Attribute", backref="projects") 

    # Architecture pattern asociated
    architecture_pattern_id = Column(Integer, ForeignKey("architecture_patterns.id"))
    architecture_pattern = relationship('ArchitecturePattern', foreign_keys='Project.architecture_pattern_id')


class ArchitecturePattern(Base):
    __tablename__ = "architecture_patterns"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)  #Pensamos que puede ser unique en un futuro.
    description = Column(String)
    #team = relationship("User", secondary=project_user_table)
    attributes = relationship("Attribute", backref="projects") 