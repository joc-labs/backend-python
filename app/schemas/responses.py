from pydantic import BaseModel
from typing import Optional, Union


class GenericResponse(BaseModel):
    success: bool = True
    message: Optional[str]
