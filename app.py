from fastapi import FastAPI,HTTPException
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
async def add_user(student: StudentModel):
    # Check if the student ID already exists
    for existing_student in students:
        if existing_student.id == student.id:
            raise HTTPException(status_code=400, detail="Please enter a different userID.")
    
    # Append the student if no duplicates are found
    students.append(student)
    return {"message": "Student created successfully", "values": student}

@app.get("/fetch_students")
def fetchStudents():
    return {"students" : students}