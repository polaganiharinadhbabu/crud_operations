from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field


app = FastAPI(title="Student Management API")


class StudentCreate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
    course: str
    age: int


class Student(StudentCreate):
    id: int


students = []
next_id = 1


@app.post(
    "/students",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def create_student(student: StudentCreate):
    global next_id

    new_student = Student(
        id=next_id,
        **student.model_dump()
    )

    students.append(new_student)
    next_id += 1

    return new_student


@app.get("/students", response_model=list[Student])
def get_students():
    return students


@app.get("/students/search", response_model=list[Student])
def search_students(course: str):
    result = []

    for student in students:
        if course.lower() in student.course.lower():
            result.append(student)

    return result


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentCreate):
    for i, existing_student in enumerate(students):
        if existing_student.id == student_id:
            updated_student = Student(
                id=student_id,
                **student.model_dump()
            )

            students[i] = updated_student

            return updated_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, student in enumerate(students):
        if student.id == student_id:
            students.pop(i)

            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )