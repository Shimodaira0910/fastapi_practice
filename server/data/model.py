from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4, UUID

class TaskModel(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    titile: str
    description: str
    completed: bool

