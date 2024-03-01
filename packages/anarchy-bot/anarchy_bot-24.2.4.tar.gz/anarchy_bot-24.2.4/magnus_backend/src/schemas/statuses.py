from typing import Dict
from pydantic import BaseModel


class ResponseStatus(BaseModel):
    status: bool
    message: str
    payload: Dict = {}
