from pydantic import BaseModel, Field
from typing import Optional


class GradesStatsResponse(BaseModel):
    count: int = Field(ge=0)
    min: Optional[int] = None
    max: Optional[int] = None
    avg: Optional[float] = None
