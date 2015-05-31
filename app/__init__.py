from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment


bootstrap = Bootstrap()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object('config')
    bootstrap.init_app(app)   

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
