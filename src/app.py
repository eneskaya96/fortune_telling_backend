from typing import Any
from flask import Flask

from src.config import ConfigManager


def create_app() -> Flask:
    app = Flask(__name__)

    config = ConfigManager.init_config()
    app.config.from_object(config)

    from src.logs.log_manager import LogManager
    LogManager.init_logger(config)

    from src.database.db_manager import DBManager
    DBManager.start_db()

    # Add tasks
    from src.tasks import cron_job

    from flask_cors import CORS
    CORS(app)

    from src.helpers.api_manager import APIManager
    APIManager(app)

    return app
