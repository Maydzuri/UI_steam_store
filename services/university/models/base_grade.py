from pydantic import BaseModel, ConfigDict, Field

from .grade_constants import MAX_GRADE, MIN_GRADE


class BaseGrade(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int = Field(ge=0)
    student_id: int = Field(ge=0)
    grade: int = Field(ge=MIN_GRADE, le=MAX_GRADE)
