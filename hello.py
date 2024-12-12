from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

## step 1 : define base

Base = declarative_base()

## step 2 : create simple table 

class Student(Base):
    __tablename__ = "SG-Ki-Table"
    id = Column(Integer,primary_key=True)
    name = Column(String(12),nullable=False)
    age = Column(Integer)

## step 3 : Connect to SQL Lite Database 

engine = create_engine("sqlite:///student.db") ## create a sqllite Database 
Base.metadata.create_all(engine) # creates tabel in the database

## step 4 : Create a session 
Session = sessionmaker(bind=engine)
session = Session() 

## step 5 : Add a student record 
new_student = Student(name="John-Wick", age=41) # create a new student (row)
session.add(new_student) # add student to session
session.commit()

print("\nstudent added successfully :-}") 
print("What a pain in ASS!")
