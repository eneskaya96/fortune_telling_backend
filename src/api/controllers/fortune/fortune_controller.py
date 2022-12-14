from flask import Response, request
from flask_restx import Namespace, Resource

from src.api.controllers import create_schemas
from src.api.controllers.fortune import auth
from src.api.models.base_response import BaseResponse
from src.api.models.dto.fortune.fortune_request_dto import FortuneRequestDto
from src.api.models.dto.fortune.fortune_response_dto import FortuneResponseDto
from src.api.services.fortune_api_service import FortuneApiService

api = Namespace('fortune', description='API for fortune')

used_schemas = create_schemas(api)

# request dto
fortune_request_schema = api.schema_model(
    'fortune_request_schema',
    FortuneRequestDto.schema()
)
# response dto
fortune_response_schema = api.schema_model(
    'fortune_response_schema',
    BaseResponse[FortuneResponseDto].schema()
)


@api.route('')
class FortuneCRUD(Resource):
    @api.doc(description='Returns random fortune', security='api_key')
    @api.response(200, 'OK', fortune_response_schema)
    @auth.login_required
    def get(self) -> Response:
        fortune_api_service = FortuneApiService()
        fortune = fortune_api_service.get_random_fortune()
        fortune_response_dto = FortuneResponseDto.create(fortune)
        return BaseResponse.create_response(message='Fortune obtained.', data=fortune_response_dto)

    @api.doc(description='Create new fortune', security='api_key')
    @api.expect(*used_schemas, fortune_request_schema)
    @api.response(200, 'OK', fortune_response_schema)
    @auth.login_required
    def post(self) -> Response:
        fortune_request_dto: FortuneRequestDto = FortuneRequestDto.parse_obj(
            request.get_json()
        )

        fortune_api_service = FortuneApiService()
        new_fortune = fortune_api_service.create_fortune(fortune_request_dto)
        fortune_response_dto = FortuneResponseDto.create(new_fortune)
        return BaseResponse.create_response(message='Fortune created.', data=fortune_response_dto)
