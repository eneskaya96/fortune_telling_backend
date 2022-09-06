import base64
from typing import Optional, Any, TypeVar, Type, List
from urllib.parse import urljoin

import requests
from requests import PreparedRequest, Response
from requests.adapters import HTTPAdapter
from requests.auth import AuthBase

from src.api.models.base_response import BaseResponse

from src.api.models.dto.fortune.fortune_request_dto import FortuneRequestDto
from src.configs.config_manager import WorkerConfigManager
from src.domain.seed_work.error.configuration_error import ConfigurationError

Model = TypeVar('Model')


class FortuneApiAuthBase(AuthBase):
    def __init__(self, username: str, password: str) -> None:
        encoded_auth_bytes = base64.b64encode(f'{username}:{password}'.encode('utf-8'))
        self.token = encoded_auth_bytes.decode('utf-8')

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        r.headers['Authorization'] = f'Basic {self.token}'
        r.headers['User-Agent'] = 'fortune-api'
        return r


class FortuneApiClient:
    __auth: Optional[FortuneApiAuthBase] = None

    __create_fortune_url = 'fortune_teller/v1/fortune'

    @classmethod
    def __get_endpoint(cls, service_url: str) -> str:
        base_url = WorkerConfigManager.config.FORTUNE_API_URL
        if not base_url:
            raise ConfigurationError(
                'Fortune API URL must be set.', 'invalid_fortune_api_url')

        return urljoin(base_url, service_url)

    @classmethod
    def __get_auth(cls) -> FortuneApiAuthBase:
        if not cls.__auth:
            username = WorkerConfigManager.config.AUTH_USERNAME
            password = WorkerConfigManager.config.AUTH_PASSWORD
            if not username or not password:
                raise ConfigurationError(
                    'Fortune Basic Authentication must be set', 'invalid_fortune_api_credentials')
            cls.__auth = FortuneApiAuthBase(
                username=username, password=password)

        return cls.__auth

    @staticmethod
    def __send_request(method: str,
                       url: str,
                       **kwargs: Any) -> Response:
        with requests.Session() as session:
            if retry := WorkerConfigManager.config.FORTUNE_API_NUMBER_OF_RETRIES > 0:
                adapter = HTTPAdapter(max_retries=retry)
                session.mount('http://', adapter)
                session.mount('https://', adapter)

            kwargs['timeout'] = (WorkerConfigManager.config.FORTUNE_API_CONNECT_TIMEOUT,
                                 WorkerConfigManager.config.FORTUNE_API_READ_TIMEOUT)

            response = session.request(method, url, **kwargs)

        return response

    @staticmethod
    def __check_response(response: Response) -> None:
        response.raise_for_status()
        if response.content:
            base_response = BaseResponse[Any].parse_obj(response.json())
            if not base_response.success:
                raise Exception(f'FortuneApi error, message: {base_response.message}')

    @staticmethod
    def __check_response_and_get_data(response: Response, model: Type[Model]) -> Optional[Model]:
        response.raise_for_status()
        base_response = BaseResponse[model].parse_obj(response.json())  # type: ignore
        if not base_response.success:
            raise Exception(f'FortuneApi error, message: {base_response.message}')
        return base_response.data

    @classmethod
    def create_fortune(cls, fortune: str) -> \
            None:
        fortune_request = FortuneRequestDto(
            fortune=fortune
        )
        endpoint = cls.__get_endpoint(f'{cls.__create_fortune_url}')
        response = cls.__send_request(
            method='POST',
            url=endpoint,
            json=fortune_request,
            auth=cls.__get_auth()
        )
        cls.__check_response(response)
