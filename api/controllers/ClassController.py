from database import db, Class
from typing import Optional
from fastapi import HTTPException
from fastapi.responses import JSONResponse

def getClasses(id: Optional[int] = None):
    """
    Retrieve all classes from the database, or a specific class by id.
    
    Args:
        id (Optional[int]): The ID of the class to retrieve. If not provided, retrieves all classes.
    
    Returns:
        list: A list of Class objects (or a single Class object if id is provided).
    """
    if id is not None:
        # Si se pasa un id, buscar la clase por id
        clase = Class.query.get(id)
        if clase:
            return clase  # Devuelve una clase individual
        else:
            raise HTTPException(status_code=404, detail=f"Clase con ID {id} no encontrada")
    else:
        # Si no se pasa un id, devolver todas las clases
        classes = Class.query.all()
        return classes


def newClass(date: str, time: int, price: int, paid: bool, student_id: int):
    """
    Create a new class in the database.
    
    Args:
        date (str): Date of the class.
        time (int): Time of the class.
        price (int): Price of the class.
        paid (bool): Whether the class has been paid or not.
        student_id (int): ID of the student associated with the class.
    
    Returns:
        tuple: A dictionary with a success message and class ID, and the HTTP status code.
    """
    # Validate parameters
    if not date or not time or price is None or paid is None or not student_id:
        raise HTTPException(status_code=400, detail="All fields are required")

    # Create new class
    new_class = Class(date=date, time=time, price=price, paid=paid, student_id=student_id)
    db.session.add(new_class)
    db.session.commit()

    return JSONResponse(content={"message": "Class created successfully", "id": new_class.id}, status_code=201)


def updateClass(id: int, class_data):
    """
    Update an existing class in the database.
    
    Args:
        id (int): ID of the class to be updated.
        class_data (dict): Dictionary containing updated class information.
    
    Returns:
        tuple: A dictionary with a success or error message and the HTTP status code.
    """
    # Search class in database
    class_obj = Class.query.get(id)
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    
    print('pagado: ' + str(class_data.paid))
    
    # Update class values
    if class_data.date:
        class_obj.date = class_data.date
    if class_data.time:
        class_obj.time = class_data.time
    if class_data.price:
        class_obj.price = class_data.price
    if class_data.paid != None:
        class_obj.paid = class_data.paid
    if class_data.student_id:
        class_obj.student_id = class_data.student_id
    
    db.session.commit()

    return JSONResponse(content={"message": "Class updated successfully"}, status_code=200)


def removeClass(id: int):
    """
    Remove a class from the database.
    
    Args:
        id (int): ID of the class to be deleted.
    
    Returns:
        tuple: A dictionary with a success or error message and the HTTP status code.
    """
    # Search class in database
    class_obj = Class.query.get(id)
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    
    # Remove class
    db.session.delete(class_obj)
    db.session.commit()

    return JSONResponse(content={"message": "Class deleted successfully"}, status_code=200)
