from typing import Optional

from flask import Flask
from flask_restx import Api

from src.api.controllers.fortune import fortune_teller_api
from src.api.controllers.fortune.fortune_controller import api as fortune_api


class APIManager:
    def __init__(self, app: Flask) -> None:
        self.api: Optional[Api] = None
        self.init_apis(app)

    def init_apis(self, app: Flask) -> None:
        self.api = Api(
            fortune_teller_api,
            title='SaaS Fortune API',
            version='0.0.1',
            description='Provides functionalities for Saas'
        )

        self.api.add_namespace(fortune_api)

        app.register_blueprint(fortune_teller_api)
