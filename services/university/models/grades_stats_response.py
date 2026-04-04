from pydantic import BaseModel, Field, model_validator


class GradesStatsResponse(BaseModel):
    count: int = Field(ge=0)
    min: int | None = Field(...)
    max: int | None = Field(...)
    avg: float | None = Field(...)

    @model_validator(mode='after')
    def validate_stats(self) -> 'GradesStatsResponse':
        if self.count == 0:
            if self.min is not None or self.max is not None or self.avg is not None:
                raise ValueError(
                    f"При count=0 ожидались None, получены min={self.min}, max={self.max}, avg={self.avg}"
                )
        else:
            if self.min is None or self.max is None or self.avg is None:
                raise ValueError(
                    f"При count>0 поля min/max/avg не могут быть None"
                )
            if not (self.min <= self.avg <= self.max):
                raise ValueError(
                    f"Некорректная статистика: min={self.min}, avg={self.avg}, max={self.max}"
                )
        return self
