from typing import List, Any

from flask_restx import Namespace

from src.api.models.dto.fortune.fortune_request_dto import FortuneRequestDto
from src.api.models.dto.fortune.fortune_response_dto import FortuneResponseDto


# define model schemas here to register them only once. auth_controller registers these schemas.
def create_schemas(api: Namespace) -> List[Any]:
    return [
        # request dtos
        api.schema_model('FortuneRequestDto', FortuneRequestDto.schema()),

        # response dtos
        api.schema_model('FortuneResponseDto', FortuneResponseDto.schema()),

        # domain models
    ]
