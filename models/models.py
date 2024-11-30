from pydantic import BaseModel
from typing import Optional

class StudentModel(BaseModel):
    id : int
    name : str
    divison : Optional[int] = None 


class UpdateStudentModel(BaseModel):
    id : int 
    name : Optional[str] = None 
    divison : Optional[int] = None 