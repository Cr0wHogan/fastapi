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
        


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email ya está registrado")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user


@app.post("/users/{user_id}/projects/", response_model=schemas.Project)
def create_project_for_user(
    user_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)
):
    return crud.create_user_project(db=db, project=project, user_id=user_id)


@app.get("/projects/", response_model=List[schemas.Project])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = crud.get_projects(db, skip=skip, limit=limit)
    return projects

    
@app.get("/projects/{project_id}", response_model=schemas.Project)
def get_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return db_project

@app.get("/users/email/{user_email}", response_model=schemas.User)
def get_users_by_email(user_email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="El usuario no participa de ningún proyecto")
    return db_user


@app.post("/project/add/{project_id}/{user_id}", response_model=schemas.Project)
def add_user_to_project(
    user_id: int,project_id:int, project: schemas.Project, db: Session = Depends(get_db)
):
    return crud.add_user_to_existent_project(db=db, project=project,project_id=project_id, user_id=user_id)


