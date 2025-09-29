from fastapi import FastAPI
from database import engine,Base
from routes import students,checkIn

app= FastAPI()
Base.metadata.create_all(engine)

@app.get('/')
def homepage():
    return {"student check-in System"}

app.include_router(students.router)
app.include_router(checkIn.router)

     