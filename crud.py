import models, schemas
from sqlalchemy.orm import Session



# Users

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

# Patterns

def similarity(attributes1, attributes2):
    return 1

def get_patterns(db: Session, project:schemas.Project):
    # Obtengo atributos
    project_attributes = project.attributes

    all_projects = db.query(models.Project).filter(models.Project.id != project.id).all()

    # tuplas (distancia, proyecto) para cada proyecto
    distances = [(similarity(p.attributes,project_attributes), p) for p in all_projects]

    # sort by distance
    distances = sorted(distances, key=lambda x: x[0])

    closest_sim = distances[0][0]
    # if the distances between the architecture and the next is lower to this then they are close enough
    treshold = 1

    # Load all who are closer between than treshold
    closest = []
    for distance, project_to_compare in distances:
        if abs(distance-closest_sim) < treshold:
            closest.append(project_to_compare)

    return closest


# Un usuario crea un proyecto
def create_pattern(db: Session, pattern: schemas.ArchitecturePatternCreate):
    # Creo el proyecto
    db_pattern = models.ArchitecturePattern(**pattern.dict())
    # Lo agrego a la base
    db.add(db_pattern)
    # Commit y refresh
    db.commit()
    db.refresh(db_pattern)
    return db_pattern

def get_pattern(db: Session, pattern_id: int):
    return db.query(models.ArchitecturePattern).filter(models.ArchitecturePattern.id == pattern_id).first()

def get_patterns(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ArchitecturePattern).offset(skip).limit(limit).all()


# Projects

def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()


# Un usuario crea un proyecto
def create_user_project(db: Session, project: schemas.ProjectCreate):
    # Creo el proyecto
    db_project = models.Project(**project.dict())
    # Traigo el objeto usuario que lo creo
    #user = db.query(models.User).filter(models.User.id == user_id).first()
    # Agrego el usuario a la tabla de asociacion de projectos y rezo que se agregue en ambos
    #db_project.team.append(user)
    #user.projects.append(db_project)
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

#Attribute templates

def create_attribute_template(db: Session, attribute_template: schemas.AttributeTemplateCreate):
    #fake_hashed_password = user.password + "notreallyhashed"
    db_attribute_template = models.AttributeTemplate(**attribute_template.dict())#, hashed_password=fake_hashed_password)
    db.add(db_attribute_template)
    db.commit()
    db.refresh(db_attribute_template)
    return db_attribute_template

def get_attribute_template_by_id(db: Session, attribute_template_id:int):
    return db.query(models.AttributeTemplate).filter(models.AttributeTemplate.id == attribute_template_id).first()

def get_attribute_template_by_slug(db: Session, slug:str):
    db_template = db.query(models.AttributeTemplate).filter(models.AttributeTemplate.slug == slug).first()
    return db_template

def get_attribute_templates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AttributeTemplate).offset(skip).limit(limit).all()



#Attributes

def get_attributes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Attribute).offset(skip).limit(limit).all()

def get_attribute_by_id(db: Session, attribute_id:str):
    return db.query(models.Attribute).filter(models.Attribute.id == attribute_id).first()

def get_or_create_attribute_with_template(db:Session,db_project:models.Project,template_id:int):
    for attribute in db_project.attributes:
        if attribute.template_id == template_id:
            return attribute

    # si no lo encuentro ->  Creo un atributo al proyecto desde su respectivo template
    db_attribute = models.Attribute(template_id=template_id,project_id=db_project.id,prioridad=0)
    db.add(db_attribute)
    db.commit()
    db.refresh(db_attribute)
    return db_attribute

def add_requirement_to_attribute(db:Session,db_attribute:models.Attribute, requirement_text: str):
    # si lo encuentro -> prioridad + 1
    db_attribute.prioridad=db_attribute.prioridad+1
    db.commit()
    # añadir requerimiento al atributo y ¿¿¿ sumar uno a prioridad # update ????
    db_requirement = models.Requirement(description=requirement_text,attribute_id=db_attribute.id)
    db.add(db_requirement)
    db.commit()
    db.refresh(db_requirement)
    return db_requirement

# Un atributo existente 
def create_attribute_from_template(db: Session, attribute: schemas.AttributeCreate):
    # Creo el atributo
    db_attribute = models.Attribute(**attribute.dict())
    # Lo agrego a la base
    db.add(db_attribute)
    # Commit y refresh
    db.commit()
    db.refresh(db_attribute)
    return db_attribute



# Requirements

def create_requirement(db: Session, requirement: schemas.RequirementCreate):
    db_requirement = models.Requirement(**requirement.dict())
    #attribute=db.query(models.Attribute).filter(models.Attribute.id == attribute_id).first()
    #attribute.requirements.append(db_requirement)
    db.add(db_requirement)
    db.commit()
    db.refresh(db_requirement)
    return db_requirement 

def get_requirement_by_id(db: Session, requirement_id:str):
    return db.query(models.Requirement).filter(models.Requirement.id == requirement_id).first()

def get_requirements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Requirement).offset(skip).limit(limit).all()