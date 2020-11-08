import models, schemas
from sqlalchemy.orm import Session

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    #fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email)#, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()


# Un usuario crea un proyecto
def create_user_project(db: Session, project: schemas.ProjectCreate, user_id: int):
    # Creo el proyecto
    db_project = models.Project(**project.dict())
    # Traigo el objeto usuario que lo creo
    user = db.query(models.User).filter(models.User.id == user_id).first()
    # Agrego el usuario a la tabla de asociacion de projectos y rezo que se agregue en ambos
    #db_project.team.append(user)
    user.projects.append(db_project)
    # Lo agrego a la base
    db.add(db_project)
    # Commit y refresh
    db.commit()
    db.refresh(db_project)
    return db_project


# Un usuario crea un proyecto
def add_user_to_project(db: Session, project_id: int, user_id: int):
    # Creo el proyecto
    user = db.query(models.User).filter(models.User.id == user_id).first()
    # Traigo el objeto usuario que lo creo
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    user.projects.append(project)
    # Lo agrego a la base
    db.commit()
    db.refresh(user)
    db.refresh(project)
    return project

def create_attribute_template(db: Session, attribute_template: schemas.AttributeTemplateCreate):
    #fake_hashed_password = user.password + "notreallyhashed"
    db_attribute_template = models.AttributeTemplate(**attribute_template.dict())#, hashed_password=fake_hashed_password)
    db.add(db_attribute_template)
    db.commit()
    db.refresh(db_attribute_template)
    return db_attribute_template

def get_attribute_templates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AttributeTemplate).offset(skip).limit(limit).all()

def get_attributes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Attribute).offset(skip).limit(limit).all()


# Un atributo existente 
def create_attribute_from_template_and_add_it_to_a_project(db: Session, attribute: schemas.AttributeCreate,template_id: int,project_id:int):
    # Creo el atributo
    db_attribute = models.Attribute(**attribute.dict(),template_id=template_id,project_id=project_id)
    # Lo agrego a la base
    db.add(db_attribute)
    # Commit y refresh
    db.commit()
    db.refresh(db_attribute)
    return db_attribute

def create_requirement(db: Session, requirement: schemas.RequirementCreate):
    db_requirement = models.Requirement(**requirement.dict())
    #attribute=db.query(models.Attribute).filter(models.Attribute.id == attribute_id).first()
    #attribute.requirements.append(db_requirement)
    db.add(db_requirement)
    db.commit()
    db.refresh(db_requirement)
    return db_requirement 
