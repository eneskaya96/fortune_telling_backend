from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from src.configs.config_manager import ApiConfigManager
    config = ApiConfigManager.init_config()
    app.config.from_object(config)

    from src.api.helpers.error_handler import ErrorHandler
    ErrorHandler.initialize(app)

    from src.infrastructure.logging.log_manager import LogManager
    LogManager.init_logger(config)

    from src.api.helpers.api_manager import APIManager
    APIManager(app)

    from flask_cors import CORS
    CORS(app)

    from src.infrastructure.db.db_manager import DBManager
    #DBManager.start_db(app)

    from src.infrastructure.persistence.redis_manager import RedisManager
    RedisManager.init_redis(config)

    from src.api.injection import ContainerManager
    ContainerManager.init_containers()

    from src.infrastructure.security.basic_auth_manager import BasicAuthManager
    BasicAuthManager.init_basic_auth_manager(app, config)

    return app

