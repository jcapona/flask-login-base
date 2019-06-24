import os
from flask import Flask
from flask_login import LoginManager


from api.config import config


def create_app():
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "dev")
    app.config.from_object(config[env])

    # Register db to the app
    from api.models import db
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login.login_route'
    login_manager.init_app(app)

    from api.models import Person

    @login_manager.user_loader
    def load_user(user_id):
        return Person.query.get(int(user_id))



    # Register blueprints for main sections of the app

    from .blueprints.login import login as login_blueprint
    app.register_blueprint(login_blueprint)

    from .blueprints.generic import generic as generic_blueprint
    app.register_blueprint(generic_blueprint)

    return app

