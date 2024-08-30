from datetime import timedelta


class Config:
    """
    configuration settings
    """
    DEBUG = True
    SECRET_KEY = "uRo4wKfxfjQ04gqKPD33Kw"
    SQLALCHEMY_DATABASE_URI = "sqlite:///plananddream.db"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    HOST = "127.0.0.1"
    PORT = 5000
