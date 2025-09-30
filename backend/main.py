from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import students, checkIn, admin
from database import Base, engine

app = FastAPI()

origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(students.router)
app.include_router(checkIn.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "Student Check-in System API is running"}
