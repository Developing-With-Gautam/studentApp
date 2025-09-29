from pydantic import BaseModel,Field,EmailStr


class Students_data(BaseModel):
    name:str = Field(...,nullable=False,description="Enter name of student")
    email:EmailStr=Field(...,nullable=False,description="Enter the email of student")
    student_id:str =Field(...,unique=True,description="Enter the studentId")

class Check_in(BaseModel):
    student_id:int =Field(...,unique=True,description="Enter the studentId")



