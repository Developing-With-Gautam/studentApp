from pydantic import BaseModel,Field,EmailStr
from typing import Optional

class admin_register(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=4)


class admin_login(BaseModel):
    email:EmailStr = Field(...,nullable=False)
    password:str= Field(...,nullable=False)

class Token(BaseModel):
    access_token :str
    token_type:str

class tokenData(BaseModel):
    email :Optional[str]=None