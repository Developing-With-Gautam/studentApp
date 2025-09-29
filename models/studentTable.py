from database import Base
from sqlalchemy import Integer,String,Column,DateTime
from sqlalchemy.orm import 


class Student_table(Base):
    __tablename__ ="student"
    id = Column(Integer,autoincrement=True,index=True,primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)

class Checkin_table(Base):
    __tablename__= "student_checkin"
    id=Column(Integer,primary_key=True,index=True)
    timestamp = Column(DateTime,default=DateTime.utcnow)


