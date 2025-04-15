from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
##############################################################################################################
app = FastAPI()
##############################################################################################################
schools = {
    "IT School": {
        "name": "IT School",
        "room": [421, 122, 231],
        "teacher": ["Bekzod", "Akbar", "Ali"],
        "students": []
    }
}

students = {
    "Muhammadqodir": {
        "name": "Muhammadqodir",
        "age": 20,
        "school": "IT School"
    }
}
##############################################################################################################
class StudentCreate(BaseModel):
    name: str
    age: int
    school: str
##############################################################################################################
class SchoolCreate(BaseModel):
    name: str
    room: List[int]
    teacher: List[str]
##############################################################################################################
@app.get("/api/school")
async def get_schools():
    return {"data": list(schools.values())}
##############################################################################################################
@app.get("/api/student")
async def get_students(school: str = None):
    if school:
        return {"data": [s for s in students.values() if s["school"] == school]}
    return {"data": list(students.values())}
##############################################################################################################
@app.get("/api/student/{student_name}")
async def get_student(student_name: str):
    student = students.get(student_name)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"data": student}
##############################################################################################################
@app.get("/api/school/{school_name}")
async def get_school(school_name: str):
    school = schools.get(school_name)
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    return {"data": school}
##############################################################################################################
@app.post("/api/student")
async def create_student(student: StudentCreate):
    if student.school not in schools:
        raise HTTPException(status_code=400, detail="School not found")
    students[student.name] = student.model_dump()  # Use model_dump() instead of dict()
    schools[student.school]["students"].append(student.name)
    return {"data": student.model_dump()}  # Use model_dump() instead of dict()
##############################################################################################################
@app.post("/api/school")
async def create_school(school: SchoolCreate):
    if school.name in schools:
        raise HTTPException(status_code=400, detail="School already exists")
    schools[school.name] = school.model_dump()  # Use model_dump() instead of dict()
    return {"data": school.model_dump()}  # Use model_dump() instead of dict()
##############################################################################################################
@app.get("/api/student")
async def get_students_by_school(school: str):
    if school not in schools:
        raise HTTPException(status_code=404, detail="School not found")
    return {"data": [student for student in students.values() if student["school"] == school]}
##############################################################################################################
@app.get("/api/school/{school_name}/rooms/count")
async def get_school_rooms_count(school_name: str):
    school = schools.get(school_name)
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    return {"count": len(school["room"])}

##############################################################################################################
@app.get("/api/student/{student_name}/details")
async def get_student_details(student_name: str):
    student = students.get(student_name)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
##############################################################################################################
@app.get("/api/school/{school_name}/teachers/count")
async def get_school_teachers_count(school_name: str):
    school = schools.get(school_name)
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    return {"count": len(school["teacher"])}
##############################################################################################################