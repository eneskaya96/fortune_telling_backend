from flask import Blueprint
from flask_httpauth import HTTPBasicAuth

from src.configs.config_manager import ApiConfigManager

fortune_teller_api = Blueprint('fortune_teller_api', __name__, url_prefix='/fortune_teller/v1')

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username: str, password: str) -> bool:
    return username == ApiConfigManager.config.AUTH_USERNAME and password == ApiConfigManager.config.AUTH_PASSWORD
