from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Student Model
class Student(BaseModel):
    id: int
    name: str
    marks: int

# In-memory database
students_db = []

# POST: Add a student
@app.post("/students", response_model=Student)
def add_student(student: Student):
    students_db.append(student)
    return student

# GET: All students OR students with marks 
@app.get("/students", response_model=List[Student])
def get_students(min_marks: Optional[int] = Query(None)):
    if min_marks is not None:
        return [s for s in students_db if s.marks > min_marks]
    return students_db
