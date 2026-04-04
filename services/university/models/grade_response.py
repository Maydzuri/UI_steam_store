from pydantic import BaseModel, ConfigDict


class GradeResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    teacher_id: int
    student_id: int
    grade: int
