
from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None