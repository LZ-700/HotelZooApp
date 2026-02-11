from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'bp.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    from app import models  # make sure models are imported

    return app


from app.models import User

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
