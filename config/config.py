import os

class Config():
    SECRET_KEY = os.getenv('SECRET_KEY',None)
    SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME',None)
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'    
    PROPAGATE_EXCEPTIONS = True
    API_TITLE = "Prueba Tecnica Globant REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', None)    

class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_DEBUG = True
    TESTING = True
    FLASK_ENV = 'development'
    
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    FLASK_ENV = 'production'
    

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}