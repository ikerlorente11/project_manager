from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from database import flask_app
from models.Student import Student as BaseStudent
from models.Class import Class as BaseClass
from controllers.StudentController import getStudents, newStudent, updateStudent, removeStudent, payClasses
from controllers.ClassController import getClasses, newClass, updateClass, removeClass
from typing import Optional

# Init app
app = FastAPI()

# Permitted origins
origins = [
    'http://localhost:4321',
    'http://localhost:3000',
    'http://gestor_clases_front:3000',
    'http://gestor_clases_front:4321',
    'https://serveriker.ddns.net:3000',
    'https://serveriker.ddns.net:4321',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear un router para todas las rutas
router = APIRouter()

# Working
@router.get("/")
def root():
    return {"message": "OK"}

# ENDPOINTS
# List students
@router.get("/students", tags=["Student"])
def listStudents(id: Optional[int] = None):
    with flask_app.app_context():
        return getStudents(id)

# Create student
@router.post("/students", tags=["Student"])
def createStudent(student: BaseStudent):
    with flask_app.app_context():
        return newStudent(student.name, student.price)

# Update student
@router.put("/students/{id}", tags=["Student"])
def modifyStudent(id: int, student: BaseStudent):
    with flask_app.app_context():
        return updateStudent(id, student)

# Delete student
@router.delete("/students/{id}", tags=["Student"])
def deleteStudent(id: int):
    with flask_app.app_context():
        return removeStudent(id)
    
# Pay classes
@router.put("/students/pay/{id}", tags=["Student"])
def payStudent(id: int):
    with flask_app.app_context():
        return payClasses(id)
    

# List classes
@router.get("/classes", tags=["Class"])
def listClasses(id: Optional[int] = None):
    with flask_app.app_context():
        return getClasses(id)

# Create class
@router.post("/classes", tags=["Class"])
def createClass(class_obj: BaseClass):
    with flask_app.app_context():
        return newClass(class_obj.date, class_obj.time, class_obj.price, class_obj.paid, class_obj.student_id)

# Update class
@router.put("/classes/{id}", tags=["Class"])
def modifyClass(id: int, class_obj: BaseClass):
    with flask_app.app_context():
        return updateClass(id, class_obj)

# Delete class
@router.delete("/classes/{id}", tags=["Class"])
def deleteClass(id: int):
    with flask_app.app_context():
        return removeClass(id)
    
app.include_router(router, prefix="/project_manager_api")