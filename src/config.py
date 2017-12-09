class BaseConfig:
    """Base configuration"""
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False