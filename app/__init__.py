from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'main.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    
    from app.models import User  # Import User model for login manager

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    login.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    from app import models  # make sure models are imported

    return app