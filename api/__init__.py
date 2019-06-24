from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register db to the app
    from .models import db
    db.init_app(app)

    # Register blueprints for 1ain sections of the app

    from .login import login as login_blueprint
    app.register_blueprint(login_blueprint)

    from .generic import generic as generic_blueprint
    app.register_blueprint(generic_blueprint)

    return app

