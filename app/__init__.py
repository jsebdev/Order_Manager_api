from flask import Flask
from flask.json import jsonify
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_cors import CORS

import logging


def create_app(settings_module='config.dev'):
    app = Flask(__name__)

    # CORS(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(settings_module)

    jwt = JWTManager(app)

    configure_logging(app)

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
        # print(e)
        return jsonify({"msg": "something went wrong, error 500!"}), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return jsonify({"msg": "looks like what your are looking for does not exist"}), 404


def configure_logging(app):
    # delete posibles handles by default
    del app.logger.handlers[:]

    # Add default logger to loggers list
    # loggers = [app.logger, logging.getLogger('sqlalchemy')]
    loggers = [app.logger, ]
    handlers = []

    # Create a handler to write messages in console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(verbose_formatter())

    if (app.config['APP_ENV'] == app.config['APP_ENV_DEV']) or (
            app.config['APP_ENV'] == app.config['APP_ENV_TEST']):
        console_handler.setLevel(logging.INFO)
        handlers.append(console_handler)
    elif app.config['APP_ENV'] == app.config['APP_ENV_PROD']:
        console_handler.setLevel(logging.INFO)
        handlers.append(console_handler)

        # Config of SMTP Handler to send mail with loggers. But I don't have a SMTP Server
        # mail_handler = SMTPHandler((app.config['MAIL_SERVER'],
        #                             app.config['MAIL_PORT']),
        #                            app.config['DONT_REPLY_FROM_MAIL'],
        #                            app.config['ADMINS'],
        #                            '[Error][{}] The application failed'.format(
        #                                app.config['APP_ENV']),
        #                            (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']), ())
        # mail_handler.setLevel(logging.ERROR)
        # mail_handler.setFormatter(mail_handler_formater())
        # handlers.append(mail_handler)

    for log in loggers:
        for handler in handlers:
            log.addHandler(handler)
        log.propate = False
        log.setLevel(logging.DEBUG)


def verbose_formatter():
    return logging.Formatter(
        '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )


# def mail_handler_formatter():
#     return logging.Formatter(
#         '''
#             Message type:       %(levelname)s
#             Location:           %(pathname)s:%(lineno)d
#             Module:             %(module)s
#             Function:           %(funcName)s
#             Time:               %(asctime)s.%(msecs)d

#             Message:

#             %(message)s
#         ''',
#         datefmt='%d/%m/%Y %H:%M:%S'
#     )
