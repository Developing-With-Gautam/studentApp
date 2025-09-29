from fastapi import FastAPI,Depends
from database import get_db,Base,engine
from sqlalchemy.orm import Session
from scheme import student
from models import studentModel


app= FastAPI()
Base.metadata.create_all(engine)


@app.get('/')
def homepage():
    return "Student check in website"

@app.post('/students')
def add_student(data:student.Students_data , db:Session = Depends(get_db)):

    new_student = studentModel(name = data.name,email = data.email,student_id= data.student_id)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
    

