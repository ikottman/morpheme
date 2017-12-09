import os
from flask import Flask, jsonify

def create_app():
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # register blueprints
    from src.api.text import text_blueprint
    app.register_blueprint(text_blueprint)
    from src.api.index import index_blueprint
    app.register_blueprint(index_blueprint)


    return app
