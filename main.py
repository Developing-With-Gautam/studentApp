from fastapi import FastAPI,Depends,HTTPException,status
from database import engine,get_db,Base
from sqlalchemy.orm import Session
from scheme import students
from models import studentsModel

app= FastAPI()
Base.metadata.create_all(engine)


@app.get('/')
def homepage():
    return "Student check in website"

@app.post('/students',status_code=status.HTTP_201_CREATED)
def add_student(data:students.Students_data , db:Session = Depends(get_db)):
    isStudentexist  = db.query(studentsModel.StudentUserModel).filter( studentsModel.StudentUserModel.student_id == data.student_id).first()
    if isStudentexist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail= f"student is already existed")
    
    new_student = studentsModel.StudentUserModel(name = data.name,email = data.email,student_id= data.student_id)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get('/students')
def get_students(db:Session = Depends(get_db)):
    return db.query(studentsModel.StudentUserModel).all()


@app.get('/students/{student_id}')
def get_students_with_student_id(student_id:str, db:Session=Depends(get_db)):
    studentM = studentsModel.StudentUserModel
    student= db.query(studentM).filter(studentM.student_id== student_id).first()
    if student:
        return student
    
    raise HTTPException (status_code=404,detail=f"StudentId {student_id} not found in the database")


@app.post('/check_in',status_code= status.HTTP_201_CREATED)
def student_checkIN(student_id:students.Check_in,db:Session = Depends(get_db)):

    isValid = db.query(studentsModel.StudentUserModel).filter(studentsModel.StudentUserModel.student_id == student_id.student_id).first()

    if not isValid:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"student with student id {student_id} not found")
    
    new_checkin = studentsModel.CheckinStudentModel(studentId_fk = student_id.student_id)
    db.add(new_checkin)
    db.commit()
    db.refresh(new_checkin)
    return new_checkin

@app.get('/check_in')
def get_checkIns_student(db:Session =Depends(get_db)):

    result = db.query(studentsModel.CheckinStudentModel).all()
    return result




    
     