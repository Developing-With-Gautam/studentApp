from fastapi import Depends,HTTPException,status,APIRouter
from database import get_db
from sqlalchemy.orm import Session
from scheme import students
from models import studentsModel


router = APIRouter()

@router.post('/students',status_code=status.HTTP_201_CREATED)
def add_student(data:students.Students_data , db:Session = Depends(get_db)):
    isStudentexist  = db.query(studentsModel.StudentUserModel).filter( studentsModel.StudentUserModel.student_id == data.student_id).first()
    if isStudentexist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail= f"student is already existed")
    
    new_student = studentsModel.StudentUserModel(name = data.name,email = data.email,student_id= data.student_id)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@router.get('/students')
def get_students(db:Session = Depends(get_db)):
    return db.query(studentsModel.StudentUserModel).all()


@router.get('/students/{student_id}')
def get_students_with_student_id(student_id:str, db:Session=Depends(get_db)):
    studentM = studentsModel.StudentUserModel
    student= db.query(studentM).filter(studentM.student_id== student_id).first()
    if student:
        return student
    
    raise HTTPException (status_code=404,detail=f"StudentId {student_id} not found in the database")
