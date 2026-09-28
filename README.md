# Student Management API

A FastAPI-based RESTful API for managing student records.

## Features

- **Create Student**: `POST /students`
- **List Students**: `GET /students`
- **Search Students by Course**: `GET /students/search?course={course}`
- **Get Student by ID**: `GET /students/{student_id}`
- **Update Student**: `PUT /students/{student_id}`
- **Delete Student**: `DELETE /students/{student_id}`

## Setup & Running

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

3. Open Swagger UI Docs at:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
