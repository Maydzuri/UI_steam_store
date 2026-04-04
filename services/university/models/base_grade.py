from pydantic import BaseModel, ConfigDict, Field


class BaseGrade(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int = Field(ge=0)
    student_id: int = Field(ge=0)
    grade: int = Field(ge=0, le=5)
