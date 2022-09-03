from __future__ import annotations
from pydantic import BaseModel
from src.domain.fortune.entities.fortune import Fortune


class FortuneResponseDto(BaseModel):
    id: str
    fortune: str

    @classmethod
    def create(cls, fortune: Fortune) -> FortuneResponseDto:
        return cls(
            id=fortune.id,
            fortune=fortune.fortune
        )
