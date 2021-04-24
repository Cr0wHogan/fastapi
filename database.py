from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://nzzkycbeudadzf:1a4c6464992f23a5165e4a6bc77668a7b0254bfb1b6025d863112a8bc0f4ed82@ec2-54-147-126-202.compute-1.amazonaws.com:5432/da9er1ajr80t88" 
#engine = create_engine(
#    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
#)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engine_string = "postgres://nuilwnihsmxzvj:6b5eddf5564500a391efe4ba312465a0cbe3852feaa33972e0b34e0295663bbc@ec2-107-20-153-39.compute-1.amazonaws.com:5432/ddvfhi4kl0egq6"

engine = create_engine(engine_string)  

Base = declarative_base()