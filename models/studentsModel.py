from database import Base
from sqlalchemy import Integer,String,Column,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class StudentUserModel(Base):
    __tablename__ ="student"
    id = Column(Integer,autoincrement=True,index=True,primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    student_id = Column(String,nullable= False ,unique= True)
    checkIn = relationship("CheckinStudentModel",back_populates="student")

class CheckinStudentModel(Base):
    __tablename__= "student_checkin"
    id=Column(Integer,primary_key=True,index=True)
    studentId_fk = Column(Integer,ForeignKey("student.id"))
    timestamp = Column(DateTime,default=datetime.utcnow)
    student = relationship("StudentUserModel",back_populates="checkIn")





