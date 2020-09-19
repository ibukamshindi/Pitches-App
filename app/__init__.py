from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # ....

    # Initializing flask extensions
    # bootstrap.init_app(app)
    db.init_app(app)
    bootstrap = Bootstrap(app)