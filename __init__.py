from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .main import main
    from .api import api
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')

    return app
