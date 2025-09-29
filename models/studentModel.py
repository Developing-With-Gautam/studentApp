from database import Base
from sqlalchemy import Integer,String,Column,DateTime
from sqlalchemy.orm import relationship


class StudentUserModel(Base):
    __tablename__ ="student"
    id = Column(Integer,autoincrement=True,index=True,primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)
    student_id = Column(Integer,nullable= False ,unique= True)
    checkIn = relationship("CheckinStudentModel",back_populates="student")

class CheckinStudentModel(Base):
    __tablename__= "student_checkin"
    id=Column(Integer,primary_key=True,index=True)
    studentId_fk = Column(Integer,foreign_key = "student_id")
    timestamp = Column(DateTime,default=DateTime.utcnow)
    student = relationship("StudentUserModel",back_populates="checkIn")





