from pydantic import BaseModel
from typing import Optional

class StudentModel(BaseModel):
    id : int
    name : str
    divison : Optional[int] = None 