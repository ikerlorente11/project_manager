from database import db, Student
from typing import Optional
from fastapi import HTTPException
from fastapi.responses import JSONResponse

def getStudents(id: Optional[int] = None):
    """
    Retrieve all students from the database, or a specific student by id.
    
    Args:
        id (Optional[int]): The ID of the student to retrieve. If not provided, retrieves all students.
    
    Returns:
        list: A list of Student objects (or a single Student object if id is provided).
    """
    if id is not None:
        # Si se pasa un id, buscar ese estudiante por id
        student = Student.query.get(id)
        if student:
            total_price = classesPrice(student)
            student.total_price = total_price
            return student
        else:
            raise HTTPException(status_code=404, detail=f"Estudiante con ID {id} no encontrado")
    else:
        # Si no se pasa un id, devolver todos los estudiantes
        students = Student.query.all()

        for student in students:
            total_price = classesPrice(student)
            student.total_price = total_price

        return students


def newStudent(name: str, price: int):
    """
    Create a new student in the database.
    
    Args:
        name (str): Name of the student.
        price (int): Price associated with the student.
    
    Returns:
        tuple: A dictionary with a success message and student ID, and the HTTP status code.
    """
    # Validate parameters
    if not name or not price:
        raise HTTPException(status_code=400, detail=f"Name and price are required")

    # Create new student
    new_student = Student(name=name, price=price)
    db.session.add(new_student)
    db.session.commit()

    return JSONResponse(content={"message": "Student created successfully", "id": new_student.id}, status_code=201)


def updateStudent(id: int, student_data):
    """
    Update an existing student in the database.
    
    Args:
        id (int): ID of the student to be updated.
        student_data (dict): Dictionary containing updated student information.
    
    Returns:
        tuple: A dictionary with a success or error message and the HTTP status code.
    """
    # Search student in database
    student = Student.query.get(id)
    if not student:
        raise HTTPException(status_code=404, detail=f"Estudiante con ID {id} no encontrado")
    
    # Update new values
    if student_data.name:
        student.name = student_data.name
    if student_data.price:
        student.price = student_data.price
    
    db.session.commit()

    return JSONResponse(content={"message": "Student updated successfully"}, status_code=200)


def removeStudent(id: int):
    """
    Remove a student from the database.
    
    Args:
        id (int): ID of the student to be deleted.
    
    Returns:
        tuple: A dictionary with a success or error message and the HTTP status code.
    """
    # Search student in database
    print('Estudiante: ' + str(id))
    student = Student.query.get(id)
    if not student:
        raise HTTPException(status_code=404, detail=f"Estudiante con ID {id} no encontrado")
    
    # Remove student
    db.session.delete(student)
    db.session.commit()

    return JSONResponse(content={"message": "Student deleted successfully"}, status_code=200)


def classesPrice(student, paid: Optional[bool] = False):
    """
    Retrieve the sum of the price of all classes for a student, based on whether the classes are paid or not.
    
    Args:
        student (object): Student object.
        paid (Optional[bool]): If True, sum the price of paid classes. If False, sum the price of unpaid classes. If None, sum all classes.
    
    Returns:
        dict: A dictionary with the sum of class prices and a success message or error message.
    """
    # Filtrar las clases basadas en el estado de 'paid' (pagadas o no pagadas)
    if paid is not None:
        # Filtrar por estado de pago (True o False)
        filtered_classes = [cls for cls in student.classes if cls.paid == paid]
    else:
        # Si no se pasa un valor para 'paid', considerar todas las clases
        filtered_classes = student.classes
    
    # Calcular la suma de los precios de las clases filtradas
    return sum(cls.price * (cls.time / 60) for cls in filtered_classes)

def payClasses(id: int):
    """
    Pay classes.
    
    Args:
        id (int): ID of the student to be updated.
    
    Returns:
        tuple: A dictionary with a success or error message and the HTTP status code.
    """
    # Search student in database
    student = Student.query.get(id)
    if not student:
        raise HTTPException(status_code=404, detail=f"Estudiante con ID {id} no encontrado")
    
    # Pagar cada clase
    for clase in student.classes:
        clase.paid = True
        db.session.commit()
    
    return JSONResponse(content={"message": f"Classes of student ID {student.id} paid successfully"}, status_code=200)
