from typing import Dict

from sqlalchemy import MetaData, Table, Column, Integer, DateTime, String
from sqlalchemy.orm import mapper

from src.infrastructure.entities.fortune_management.fortune import Fortune
from src.infrastructure.mappings import BaseMapper


class FortuneMapper(BaseMapper):
    def __init__(self, metadata: MetaData):
        super().__init__(metadata, Fortune)

    def perform_mapping(self, mappings: Dict[type, Table]) -> Table:
        fortune_mapping = Table(
            'fortune', self._metadata,
            Column('id', Integer, primary_key=True),
            Column('created_date', DateTime, nullable=False),
            Column('modified_date', DateTime),
            Column('fortune', String(250), nullable=False)
        )

        mapper(Fortune, fortune_mapping)

        return fortune_mapping
