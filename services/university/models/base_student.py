from pydantic import BaseModel, ConfigDict

from .degree_enum import DegreeEnum


class BaseStudent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    first_name: str
    last_name: str
    email: str
    degree: DegreeEnum
    phone: str
    group_id: int
