from fastapi import Depends,status,APIRouter
from database import get_db
from sqlalchemy.orm import Session
from scheme import students
from models import studentsModel
from repository import checkInRepo 
router = APIRouter()

@router.post('/check_in',status_code= status.HTTP_201_CREATED,tags=["student check_in"])
def student_checkIN(student_id:students.Check_in,db:Session = Depends(get_db)):
    return checkInRepo.studentCheckIN(student_id,db)


@router.get('/check_in',tags=["student check_in"])
def get_checkIns_student(db:Session =Depends(get_db)):
    result = db.query(studentsModel.CheckinStudentModel).all()
    return result


    
@router.get("/check_ins/today",tags=["student check_in"])
def total_checkins_today(db: Session = Depends(get_db)):
    return checkInRepo.totalcheckinstoday(db)
