from fastapi import status, Depends, HTTPException
from scheme import admin
from database import get_db
from sqlalchemy.orm import Session
from models import adminModel
from verification import password_verify,jwtVerification

def adminRegister(data: admin.admin_register, db: Session = Depends(get_db)):
    new_user = adminModel.Admin(
        name=data.name,
        email=data.email,
        hashPassword=password_verify.hash_password(data.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def adminLogin(data: admin.admin_login, db: Session = Depends(get_db),):
    user = db.query(adminModel.Admin).filter(adminModel.Admin.email == data.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Admin with email {data.email} not found in the database"
        )
    
    verify_password = password_verify.verify_password(data.password, user.hashPassword)

    if not verify_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password does not match"
        )

    access_token = jwtVerification.create_access_token(data = {'sub':user.email})
    return {'access_token': access_token, "token_type":"bearer"}