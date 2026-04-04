from pydantic import BaseModel, ConfigDict, Field


class GradeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int
    student_id: int
    grade: int = Field(ge=0, le=5)
