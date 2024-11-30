from fastapi import FastAPI
from models.student_model import StudentModel
from typing import List

# Main App running the server 
app  = FastAPI()

# Setting the container for storing data
students : List[StudentModel] = []

@app.get("/")
def initial_route():
    return "Hello World!"

@app.post("/add_student")
def add_user(student : StudentModel):
    students.append(student)
    return {"message" : "Student created successfully" , "values" : student}