from fastapi import FastAPI

app= FastAPI()

@app.get('/')
def homepage():
    return "Student check in website"