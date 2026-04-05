from pydantic import BaseModel, Field, model_validator
from config.settings import MIN_GRADE, MAX_GRADE


class GradesStatsResponse(BaseModel):
    count: int = Field(ge=0)
    min: int | None
    max: int | None
    avg: float | None

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
            if self.min < MIN_GRADE or self.max > MAX_GRADE:
                raise ValueError(
                    f"Оценки выходят за допустимые границы [{MIN_GRADE}, {MAX_GRADE}]: min={self.min}, max={self.max}"
                )
            if self.avg < MIN_GRADE or self.avg > MAX_GRADE:
                raise ValueError(
                    f"Средняя оценка {self.avg} выходит за границы [{MIN_GRADE}, {MAX_GRADE}]"
                )
        return self
