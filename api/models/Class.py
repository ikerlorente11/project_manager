
from pydantic import BaseModel
from typing import Optional

class Class(BaseModel):
    date: Optional[str] = None
    time: Optional[int] = None
    price: Optional[int] = None
    paid: Optional[bool] = None
    student_id: Optional[int] = None