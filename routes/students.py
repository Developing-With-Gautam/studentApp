from fastapi import Depends,status,APIRouter
from database import get_db
from sqlalchemy.orm import Session
from scheme import students
from models import studentsModel
from repository import studentsRepo


router = APIRouter()

@router.post('/students',status_code=status.HTTP_201_CREATED,tags=["Students"])
def add_student(data:students.Students_data , db:Session = Depends(get_db)):
    return studentsRepo.addstudent(data,db)

@router.get('/students',tags=["Students"])
def get_students(db:Session = Depends(get_db)):
    return db.query(studentsModel.StudentUserModel).all()


@router.get('/students/{student_id}',tags=["Students"])
def get_students_with_student_id(student_id:str, db:Session=Depends(get_db)):
    return studentsRepo.getstudentswithstudent_id(student_id,db)
   
