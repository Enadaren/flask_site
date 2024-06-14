import os

app_dir=os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'A SECRET KEY'
    SQLALCHEMY_TRACK_MODIFICATIOINS=False

class DevelopmentConfig(BaseConfig):
    DEBUG=True
    SQLALCHEMY_DATABSE_URI=os.environ.get('DEVELOPMENT_DATABASE_URI') or 'postgresql+psycopg2://alisa:alisa@localhost/recipes_db'

class TestingConfig(BaseConfig):
    DEBUG=True
    SQLALCHEMY_DATABSE_URI=os.environ.get('TESTING_DATABASE_URI') or 'postgresql+psycopg2://alisa:alisa@localhost/recipes_db'

class ProductionConfig(BaseConfig):
    DEBUG=False
    SQLALCHEMY_DATABSE_URI=os.environ.get('PRODUCTION_DATABASE_URI') or 'postgresql+psycopg2://alisa:alisa@localhost/recipes_db'