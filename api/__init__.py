import os
from flask import Flask
from api.config import config

def create_app():
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "dev")
    app.config.from_object(config[env])

    # Register db to the app
    from api.models import db
    db.init_app(app)

    # Register blueprints for main sections of the app

    from .blueprints.login import login as login_blueprint
    app.register_blueprint(login_blueprint)

    from .blueprints.generic import generic as generic_blueprint
    app.register_blueprint(generic_blueprint)

    return app

