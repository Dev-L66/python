from typing import Optional
from pydantic import BaseModel,Field
import re

class Employee(BaseModel):
    id:int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee name",
        examples="Alex"
    )
department:Optional[str] = 'General'
salary: float = Field(
    ...,
    ge=10000,
    le=1000000,
    description="Annual salary"
)


class User(BaseModel):
    email: str = Field( ..., regex=r'')
    phonr: str = Field(..., regex=r'')
    age: int = Field(..., ge=0, le=150, description="Age in years")
    discount: float = Field(..., ge=0,le=100, description="Discount")
