from database import db, Project  # Import the database session and Project model
from typing import Optional
from fastapi import HTTPException  # Import HTTPException for error handling
from fastapi.responses import JSONResponse  # Import JSONResponse for returning JSON responses

# Function to retrieve projects, either all or by a specific ID
def getProjects(id: Optional[int] = None):
    if id is not None:
        # If an ID is provided, attempt to retrieve the specific project
        project = Project.query.get(id)
        if project:
            total_price = projectsPrice(project)  # Calculate total price for the project
            project.total_price = total_price  # Add total price to the project object
            return project  # Return the found project
        else:
            # Raise a 404 error if the project is not found
            raise HTTPException(status_code=404, detail=f"Project with ID {id} not found")
    else:
        # If no ID is provided, return all projects
        projects = Project.query.all()

        # Calculate total price for each project
        for project in projects:
            total_price = projectsPrice(project)
            project.total_price = total_price

        return projects

# Function to create a new project
def newProject(name: str, price: int):
    # Validate that both name and price are provided
    if not name or not price:
        raise HTTPException(status_code=400, detail="Name and price are required")

    # Create a new Project instance
    new_project = Project(name=name, price=price)
    db.session.add(new_project)  # Add the new project to the session
    db.session.commit()  # Commit the session to save changes

    # Return a success message with the ID of the newly created project
    return JSONResponse(content={"message": "Project created successfully", "id": new_project.id}, status_code=201)

# Function to update an existing project
def updateProject(id: int, project_data):
    # Attempt to retrieve the project by ID
    project = Project.query.get(id)
    if not project:
        # Raise a 404 error if the project is not found
        raise HTTPException(status_code=404, detail=f"Project with ID {id} not found")
    
    # Update fields if new data is provided
    if project_data.name:
        project.name = project_data.name
    if project_data.price:
        project.price = project_data.price
    
    db.session.commit()  # Commit the session to save changes

    # Return a success message
    return JSONResponse(content={"message": "Project updated successfully"}, status_code=200)

# Function to remove a project by ID
def removeProject(id: int):
    # Attempt to retrieve the project by ID
    project = Project.query.get(id)
    if not project:
        # Raise a 404 error if the project is not found
        raise HTTPException(status_code=404, detail=f"Project with ID {id} not found")
    
    db.session.delete(project)  # Delete the project from the session
    db.session.commit()  # Commit the session to save changes

    # Return a success message
    return JSONResponse(content={"message": "Project deleted successfully"}, status_code=200)

# Function to calculate the total price of a project based on its registries
def projectsPrice(project, paid: Optional[bool] = False):
    # Filter registries based on the paid status if provided
    if paid is not None:
        filtered_registries = [cls for cls in project.registries if cls.paid == paid]
    else:
        filtered_registries = project.registries
    
    # Calculate the total price based on the price and time of each registry
    return sum(cls.price * (cls.time / 60) for cls in filtered_registries)

# Function to mark all registries of a project as paid
def payRegistries(id: int):
    # Attempt to retrieve the project by ID
    project = Project.query.get(id)
    if not project:
        # Raise a 404 error if the project is not found
        raise HTTPException(status_code=404, detail=f"Project with ID {id} not found")
    
    # Mark each registry of the project as paid
    for registry in project.registries:
        registry.paid = True
        db.session.commit()  # Commit the session to save changes
    
    # Return a success message
    return JSONResponse(content={"message": f"Registries of project ID {project.id} paid successfully"}, status_code=200)