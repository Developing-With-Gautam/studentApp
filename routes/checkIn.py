from fastapi import Depends,HTTPException,status,APIRouter
from database import get_db
from sqlalchemy.orm import Session
from scheme import students
from models import studentsModel
from datetime import datetime,date,timedelta
from sqlalchemy import func

router = APIRouter()

@router.post('/check_in',status_code= status.HTTP_201_CREATED)
def student_checkIN(student_id:students.Check_in,db:Session = Depends(get_db)):

    isValid = db.query(studentsModel.StudentUserModel).filter(studentsModel.StudentUserModel.student_id == student_id.student_id).first()

    if not isValid:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"student with student id {student_id} not found")
    
    new_checkin = studentsModel.CheckinStudentModel(studentId_fk = student_id.student_id)
    db.add(new_checkin)
    db.commit()
    db.refresh(new_checkin)
    return new_checkin

@router.get('/check_in')
def get_checkIns_student(db:Session =Depends(get_db)):

    result = db.query(studentsModel.CheckinStudentModel).all()
    return result


    
@router.get("/check_ins/today")
def total_checkins_today(db: Session = Depends(get_db)):

    today_start = datetime.combine(date.today(), datetime.min.time())
   
    today_end = datetime.combine(date.today(), datetime.max.time())

    total = (
        db.query(func.count(studentsModel.CheckinStudentModel.id))
        .filter(
            studentsModel.CheckinStudentModel.timestamp >= today_start,
            studentsModel.CheckinStudentModel.timestamp <= today_end
        )
        .scalar()
    )

    return {"total_checkins_today": total}