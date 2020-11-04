from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

association_table = Table('association', Base.metadata,
    Column('users_id', Integer, ForeignKey('users.id')),
    Column('Architectures_id', Integer, ForeignKey('users.id'))
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    #hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
   
    projects = relationship("Project", secondary=association_table, back_populates="owner")


class Project(Base):
    __tablename__ = "Architectures"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
   
    owner = relationship("User", secondary=association_table, back_populates="projects")

#class Projects(Base):
 #   __tablename__ = "Projects"
  #  id = Column(Integer, primary_key=True, ForeignKey("users.id"))
   # project = Column(Integer, primary_key=True, ForeignKey("Architectures.id"))
