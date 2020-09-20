from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_login import LoginManager

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
photos = UploadSet('photos',IMAGES)
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    # configure UploadSet
    configure_uploads(app,photos)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    