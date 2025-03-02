from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from database import flask_app
from models.Project import Project as BaseProject
from models.Registry import Registry as BaseRegistry
from controllers.ProjectController import getProjects, newProject, updateProject, removeProject, payRegistries
from controllers.RegistryController import getRegistries, newRegistry, updateRegistry, removeRegistry
from typing import Optional

# Init app
app = FastAPI()

# Permitted origins
origins = [
    'http://localhost:5321',
    'http://localhost:5322',
    'http://localhost:4201',
    'http://project_manager_front:5321',
    'http://project_manager_front:5322',
    'http://project_manager_front_angular_dev:4201',
    'https://serveriker.ddns.net:5321',
    'https://serveriker.ddns.net:5322',
]

# Set middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create router for all routes
router = APIRouter()

# Working
@router.get("/")
def root():
    return {"message": "OK"}

# ENDPOINTS
# List projects
@router.get("/projects", tags=["Project"])
def listProjects(id: Optional[int] = None):
    with flask_app.app_context():
        return getProjects(id)

# Create project
@router.post("/projects", tags=["Project"])
def createProject(project: BaseProject):
    with flask_app.app_context():
        return newProject(project.name, project.price)

# Update project
@router.put("/projects/{id}", tags=["Project"])
def modifyProject(id: int, project: BaseProject):
    with flask_app.app_context():
        return updateProject(id, project)

# Delete project
@router.delete("/projects/{id}", tags=["Project"])
def deleteProject(id: int):
    with flask_app.app_context():
        return removeProject(id)
    
# Pay registries
@router.put("/projects/pay/{id}", tags=["Project"])
def payProject(id: int):
    with flask_app.app_context():
        return payRegistries(id)
    

# List registries
@router.get("/registries", tags=["Registry"])
def listRegistries(id: Optional[int] = None):
    with flask_app.app_context():
        return getRegistries(id)

# Create registry
@router.post("/registries", tags=["Registry"])
def createRegistry(registry_obj: BaseRegistry):
    with flask_app.app_context():
        return newRegistry(registry_obj.date, registry_obj.time, registry_obj.price, registry_obj.paid, registry_obj.project_id)

# Update registry
@router.put("/registries/{id}", tags=["Registry"])
def modifyRegistry(id: int, registry_obj: BaseRegistry):
    with flask_app.app_context():
        return updateRegistry(id, registry_obj)

# Delete registry
@router.delete("/registries/{id}", tags=["Registry"])
def deleteRegistry(id: int):
    with flask_app.app_context():
        return removeRegistry(id)


# Add base url to all routes
app.include_router(router, prefix="/project_manager_api")