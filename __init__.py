from flask import Flask
from config import config

def create_app(config_name):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config[config_name])

    from .app import app
    from .api import api
    flask_app.register_blueprint(app)
    flask_app.register_blueprint(api, url_prefix='/api')

    return flask_app
