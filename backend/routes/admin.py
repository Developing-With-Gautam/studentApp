from fastapi import APIRouter, status, Depends
from scheme import admin
from database import get_db
from sqlalchemy.orm import Session
from repository import adminRepo

router = APIRouter()

@router.post("/admin", status_code=status.HTTP_201_CREATED,tags=["Admin"])
def admin_register(data: admin.admin_register, db: Session = Depends(get_db)):
    return adminRepo.adminRegister(data,db)
    

@router.post("/login",tags=["Admin"])
def admin_login(data: admin.admin_login, db: Session = Depends(get_db),):
    return adminRepo.adminLogin(data,db)