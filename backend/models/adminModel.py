from database import Base
from sqlalchemy import Integer,String,Column
class Admin(Base):
    __tablename__="admin"

    id =Column(Integer,primary_key=True,index=True,autoincrement=True)
    name = Column(String,nullable=False)
    email =Column(String,nullable=False)
    hashPassword = Column(String,nullable= False)