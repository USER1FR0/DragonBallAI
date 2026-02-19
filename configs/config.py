import os

class BaseConfig:
    APP_NAME = "Dragon Ball IA"
    DB_API_URL = "https://dragonball-api.com/api/"
    
class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False