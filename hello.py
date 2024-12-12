from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

## step 1 : define base

Base = declarative_base()

## step 2 : create simple table 

class student(Base):
    __tablename__ = "SG-Ki-Table"
    id = Column(Integer,primary_key=True)
    name = Column(String(12),nullable=False)
    age = Column(Integer)

## step 3 : Connect to SQL Lite Database 

engine = create_engine("sqlite:///student.db")
Base.metadata.create_all(engine) # creates tabel in the database
