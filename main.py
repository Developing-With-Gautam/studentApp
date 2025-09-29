from fastapi import FastAPI
from database import engine,Base


app= FastAPI()
Base.metadata.create_all(engine)

@app.get('/')
def homepage():
    return {"student check-in System"}




     