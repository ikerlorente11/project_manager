from pydantic import BaseModel
from typing import Optional

# Define a Pydantic model for the Registry entity
class Registry(BaseModel):
    # Optional field for the date of the registry, represented as a string
    date: Optional[str] = None
    
    # Optional field for the time associated with the registry, represented as an integer
    time: Optional[int] = None
    
    # Optional field for the price of the registry, represented as an integer
    price: Optional[int] = None
    
    # Optional field indicating whether the registry has been paid, represented as a boolean
    paid: Optional[bool] = None
    
    # Optional field for the project ID associated with the registry, represented as an integer
    project_id: Optional[int] = None