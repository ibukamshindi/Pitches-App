import os
class Config:
    '''
    General configuration parent class
    '''
    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://patrick:201400@localhost/pitches'
    # SECRET_KEY = os.environ.get("SECRET_KEY")
    SECRET_KEY ='huwezisahau'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.mail.yahoo.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME =os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD =os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'patodev01@yahoo.com'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI=('postgresql+psycopg2://patrick:201400@localhost/pitches')
    DEBUG = True

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI=('postgresql+psycopg2://patrick:201400@localhost/pitches')
    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}