from flask import Flask, render_template
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# import logging


def create_app(settings_module='config.prod'):
    app = Flask(__name__)

    # CORS(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(settings_module)

    jwt = JWTManager(app)

    # configure_logging(app)

    # Api Blueprint registrations
    from app.api.v1 import api
    app.register_blueprint(api)

    @app.route('/')
    def welcome():
        return "Welcome to the Order Manager API"

    # Set strict slashes to false
    app.url_map.strict_slashes = False

    # Error handlers
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    """Error handlers"""

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404


# def configure_logging(app):
#     del app.logger.handlers[:]

#     # loggers = [app.logger, logging.getLogger('sqlalchemy')]
#     loggers = [app.logger, ]
#     handlers = []

#     console_handler = logging.StreamHandler()
#     console_handler.setFormatter(verbose_formatter())
#     if (app.config['APP_ENV'] == app.config['APP_ENV_DEV']) or (
#             app.config['APP_ENV'] == app.config['APP_ENV_TEST']):
#         console_handler.setLevel(logging.DEBUG)
#         handlers.append(console_handler)
#     elif app.config['APP_ENV'] == app.config['APP_ENV_PROD']:
#         console_handler.setLevel(logging.INFO)
#         handlers.append(console_handler)

#     for log in loggers:
#         for handler in handlers:
#             log.addHandler(handler)
#         log.propate = False
#         log.setLevel(logging.DEBUG)


# def verbose_formatter():
#     return logging.Formatter(
#         '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
#         datefmt='%d/%m/%Y %H:%M:%S'
#     )
