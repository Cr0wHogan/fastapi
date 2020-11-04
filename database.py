from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgres+psycopg2://nzzkycbeudadzf:1a4c6464992f23a5165e4a6bc77668a7b0254bfb1b6025d863112a8bc0f4ed82@ec2-54-147-126-202.compute-1.amazonaws.com:5432/da9er1ajr80t88" 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()