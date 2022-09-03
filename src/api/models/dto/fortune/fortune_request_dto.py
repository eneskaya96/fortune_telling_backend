from __future__ import annotations
from pydantic import BaseModel


class FortuneRequestDto(BaseModel):
    fortune: str

