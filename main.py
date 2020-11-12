# main.py
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import crud, models, schemas
from database import sessionmaker, engine

Session = sessionmaker(engine)  
db = Session()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    #db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# # # # # # # # # #
#      USERS      #
# # # # # # # # # #

# Create users
@app.post("/users/create", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email ya está registrado")
    return crud.create_user(db=db, user=user)

# Get all users
@app.get("/users/get", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# Get user by id
@app.get("/users/get/id/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

# Get user by email
@app.get("/users/get/email/{user_email}", response_model=schemas.User)
def get_users_by_email(user_email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user




# # # # # # # # # #
#    PROJECTS     #
# # # # # # # # # #

# Create project
@app.post("/projects/create", response_model=schemas.Project)
def create_project_for_user(
    project: schemas.ProjectCreate, db: Session = Depends(get_db)
):
    return crud.create_user_project(db=db, project=project)

# Join
@app.put("/projects/join", status_code=200)
def join_project_user(
    user_id: int, project_id: int, db: Session = Depends(get_db)
):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    return crud.add_user_to_project(db=db, project_id=project_id, user_id=user_id)

# Get all projects
# TODO: agregarle el team (join query)
@app.get("/projects/get", response_model=List[schemas.Project])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = crud.get_projects(db, skip=skip, limit=limit)
    return projects

# Get one project by id
# TODO: agregarle el team (join query)
@app.get("/projects/get/{project_id}", response_model=schemas.Project)
def get_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return db_project

# Add attribute
@app.get("/projects/add_attribute", response_model=schemas.Project) #(requirement_text, attribute_name, project_id)
def add_attribute_to_project(attribute_name:str,project_id:int,requirement_text:str,db: Session = Depends(get_db)):
    # traer el template por attribute name #filter
    db_template = crud.get_attribute_template_by_slug(db, slug=attribute_name)
    #Chequeo que exista el template especificado
    if db_template is None:
        raise HTTPException(status_code=404, detail="El template del atributo no existe")
    
    # Traigo proyecto
    db_project= crud.get_project(db, project_id=project_id)
    #Chequeo que exista el proyecto
    if db_project is None:
        raise HTTPException(status_code=404, detail="El proyecto no existe")

    # Obtengo o creo el atributo
    db_attribute = crud.get_or_create_attribute_with_template(db=db,db_project=db_project,template_id=db_template.id)
    
    # Agrego el requerimiento al atributo
    db_requirement = crud.add_requirement_to_attribute(db,db_attribute,requirement_text)
    
    return db_project

# Link to pattern
@app.get("/projects/add_pattern", response_model=schemas.Project) #(requirement_text, attribute_name, project_id)
def add_attribute_to_project(pattern_id:int,project_id:int,db: Session = Depends(get_db)):
    db_project = crud.add_pattern_to_project(db,project_id,pattern_id)
    return db_project


# # # # # # # # # # # # # #
#  ARCHITECTURE PATTERNS  #
# # # # # # # # # # # # # # 

# Create pattern
@app.post("/patterns/create", response_model=schemas.ArchitecturePattern)
def create_pattern(
    pattern: schemas.ArchitecturePatternCreate, db: Session = Depends(get_db)
):
    return crud.create_pattern(db=db, pattern=pattern)

# Get all patterns
@app.get("/pattern/get", response_model=List[schemas.ArchitecturePattern])
def read_patterns(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patterns = crud.get_patterns(db, skip=skip, limit=limit)
    return patterns


# Get all patterns
@app.get("/pattern/suggestion", response_model=List[schemas.ArchitecturePattern])
def suggest_patterns(project_id: int, db: Session = Depends(get_db)):

    # Traigo proyecto
    db_project= crud.get_project(db, project_id=project_id)
    #Chequeo que exista el proyecto
    if db_project is None:
        raise HTTPException(status_code=404, detail="El proyecto no existe")

    patterns = crud.get_pattern_suggestion(db, project=db_project)
    return patterns

# # # # # # # # # # # # # #
#  ATTRIBUTES TEMPLATES   #
# # # # # # # # # # # # # # 

# Create attribute template
@app.post("/attribute_templates/create", response_model=schemas.AttributeTemplate)
def create_template(attribute_template: schemas.AttributeTemplateCreate, db: Session = Depends(get_db)):
    return crud.create_attribute_template(db=db, attribute_template=attribute_template)

# Get all attribute templates
@app.get("/attribute_templates/get", response_model=List[schemas.AttributeTemplate])
def read_templates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    templates = crud.get_attribute_templates(db, skip=skip, limit=limit)
    return templates

# Get template by id
@app.get("/attribute_templates/get/id/{attribute_template_id}", response_model=schemas.AttributeTemplate)
def read_attribute_template_by_id(attribute_template_id:str, db: Session = Depends(get_db)):
    template = crud.get_attribute_template_by_id(db,attribute_template_id=attribute_template_id)
    return template

#Get template attribute by name
@app.get("/attribute_templates/get/name/{slug}", response_model=schemas.AttributeTemplate)
def get_template_by_name(slug: str, db: Session = Depends(get_db)):
    db_template = crud.get_attribute_template_by_slug(db, slug=slug)
    if db_template is None:
        raise HTTPException(status_code=404, detail="La plantilla de atributo no existe")
    return db_template



# # # # # # # # # 
#  ATTRIBUTES   #
# # # # # # # # #

# Create attribute from template
@app.post("/attributes/create", response_model=schemas.Attribute)
def create_attribute(attribute: schemas.AttributeCreate, db: Session = Depends(get_db)):
    return crud.create_attribute_from_template(db=db, attribute=attribute)

# Get all attributes
@app.get("/attributes/get", response_model=List[schemas.Attribute])
def read_attributes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    attributes = crud.get_attributes(db, skip=skip, limit=limit)
    return attributes

# Get attribute by id
@app.get("/attributes/get/id/{attribute_id}", response_model=schemas.Attribute)
def read_attribute_by_id(attribute_id:str, db: Session = Depends(get_db)):
    attribute = crud.get_attribute_by_id(db,attribute_id=attribute_id)
    return attribute



# # # # # # # # # 
#  REQUIREMENTS #
# # # # # # # # #

# Create requirement
@app.post("/requirements/create", response_model=schemas.Requirement)
def create_requirement(requirement: schemas.RequirementCreate, db: Session = Depends(get_db)):
    return crud.create_requirement(db=db, requirement=requirement)

# Get all requirements
@app.get("/requirements/get", response_model=List[schemas.Requirement])
def read_requirements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    requirements = crud.get_requirements(db, skip=skip, limit=limit)
    return requirements

# Get requirement by id
@app.get("/requirements/get/id/{requirement_id}", response_model=schemas.Requirement)
def read_requirement_by_id(requirement_id:str,db: Session = Depends(get_db)):
    requirement = crud.get_requirement_by_id(db,requirement_id = requirement_id)
    return requirement

