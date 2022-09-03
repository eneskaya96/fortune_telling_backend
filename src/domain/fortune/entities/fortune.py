from __future__ import annotations

from src.domain.seed_work.model.base_entity_model import BaseStrEntityModel


class Fortune(BaseStrEntityModel):
    fortune: str

    class Config:
        orm_mode = True

    @classmethod
    def create_fortune(cls,
                       fortune: str) -> Fortune:
        return cls(fortune=fortune)
