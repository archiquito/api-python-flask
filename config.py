"""Configurações da aplicação"""

class Config:
    """Configurações base"""
    DEBUG = True
    HOST = '127.0.0.1'
    PORT = 8080
    JSON_SORT_KEYS = False

class DevelopmentConfig(Config):
    """Configurações de desenvolvimento"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurações de produção"""
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
