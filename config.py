import os

class Config:
    '''
    general configuration; put database url here
    '''

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