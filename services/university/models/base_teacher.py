from pydantic import BaseModel, ConfigDict

from .subject_enum import SubjectEnum


class BaseTeacher(BaseModel):
    model_config = ConfigDict(extra="forbid")

    first_name: str
    last_name: str
    subject: SubjectEnum
