from flask import Flask
from flask_bootstrap import Bootstrap
from .news.views import news
from config import configuration

bootstrap = Bootstrap()

def create_app(config_type):
    app = Flask(__name__)
    app.config.from_object(configuration[config_type])
    app.register_blueprint(news)
    bootstrap.init_app(app)

    from frontend.requests import configure_request

    configure_request(app)
    return app