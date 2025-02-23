from pydantic import BaseModel
from typing import Optional

# Define a Pydantic model for the Project entity
class Project(BaseModel):
    # Optional field for the name of the project, represented as a string
    name: Optional[str] = None
    
    # Optional field for the price of the project, represented as an integer
    price: Optional[int] = None