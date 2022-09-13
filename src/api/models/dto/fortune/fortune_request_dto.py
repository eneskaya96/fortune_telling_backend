from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel


class FortuneRequestDto(BaseModel):
    fortune: str

    def dict(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        return {
            'fortune': self.fortune
        }
