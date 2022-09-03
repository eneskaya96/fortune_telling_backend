from typing import List, Any

from flask_restx import Namespace
from src.api.models.dto.fortune.fortune_response_dto import FortuneResponseDto


# define model schemas here to register them only once. auth_controller registers these schemas.
def create_schemas(api: Namespace) -> List[Any]:
    return [
        # request dtos
        # response dtos
        api.schema_model('FortuneResponseDto', FortuneResponseDto.schema()),

        # domain models
    ]
