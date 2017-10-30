import os

class Config:
    '''
    general configuration
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gitu_m:sqlpass@localhost/pitchsite'

class ProdConfig:
    '''
    production configuration child class
    '''
    pass

class DevConfig:
    '''
    development configuration child class
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}