from fastapi import FastAPI,HTTPException
from models.models import StudentModel,UpdateStudentModel
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


@app.put("/update_student")
def updateStudent(student : UpdateStudentModel):
    student_pointer = 0;
    for existing_student in students:
        if existing_student.id == student.id:

            if(student.name != None):
                existing_student.name = student.name

            if(student.divison != None):
                existing_student.divison = student.divison
        
        else:
            raise HTTPException(status_code=404, detail="Student details not found.")
    
    return {"message" : "Student data updated successfully", "data" : student}


@app.delete("/delete_student/{student_id}")
def deleteStudent(student_id : int):
    for existing_student in students:
        if existing_student.id == student_id: 
            students.remove(existing_student)
            return {"message" : "Student data removed successfully."}

    raise HTTPException(status_code=404,detail="Student ID not found.")    