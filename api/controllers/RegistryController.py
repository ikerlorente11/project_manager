from database import db, Registry  # Import the database session and Registry model
from typing import Optional
from fastapi import HTTPException  # Import HTTPException for error handling
from fastapi.responses import JSONResponse  # Import JSONResponse for returning JSON responses

# Function to retrieve registries, either all or by a specific ID
def getRegistries(id: Optional[int] = None):
    if id is not None:
        # If an ID is provided, attempt to retrieve the specific registry
        registry = Registry.query.get(id)
        if registry:
            return registry  # Return the found registry
        else:
            # Raise a 404 error if the registry is not found
            raise HTTPException(status_code=404, detail=f"Registry with ID {id} not found")
    else:
        # If no ID is provided, return all registries
        registries = Registry.query.all()
        return registries

# Function to create a new registry
def newRegistry(date: str, time: int, price: int, paid: bool, project_id: int):
    # Validate that all required fields are provided
    if not date or not time or price is None or paid is None or not project_id:
        raise HTTPException(status_code=400, detail="All fields are required")

    # Create a new Registry instance
    new_registry = Registry(date=date, time=time, price=price, paid=paid, project_id=project_id)
    db.session.add(new_registry)  # Add the new registry to the session
    db.session.commit()  # Commit the session to save changes

    # Return a success message with the ID of the newly created registry
    return JSONResponse(content={"message": "Registry created successfully", "id": new_registry.id}, status_code=201)

# Function to update an existing registry
def updateRegistry(id: int, registry_data):
    # Attempt to retrieve the registry by ID
    registry_obj = Registry.query.get(id)
    if not registry_obj:
        # Raise a 404 error if the registry is not found
        raise HTTPException(status_code=404, detail=f"Registry with ID {id} not found")
    
    # Update fields if new data is provided
    if registry_data.date:
        registry_obj.date = registry_data.date
    if registry_data.time:
        registry_obj.time = registry_data.time
    if registry_data.price:
        registry_obj.price = registry_data.price
    if registry_data.paid is not None:
        registry_obj.paid = registry_data.paid
    if registry_data.project_id:
        registry_obj.project_id = registry_data.project_id
    
    db.session.commit()  # Commit the session to save changes

    # Return a success message
    return JSONResponse(content={"message": "Registry updated successfully"}, status_code=200)

# Function to remove a registry by ID
def removeRegistry(id: int):
    # Attempt to retrieve the registry by ID
    registry_obj = Registry.query.get(id)
    if not registry_obj:
        # Raise a 404 error if the registry is not found
        raise HTTPException(status_code=404, detail=f"Registry with ID {id} not found")
    
    db.session.delete(registry_obj)  # Delete the registry from the session
    db.session.commit()  # Commit the session to save changes

    # Return a success message
    return JSONResponse(content={"message": "Registry deleted successfully"}, status_code=200)