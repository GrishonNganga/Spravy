import os

class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?{}&apiKey={}'
    SECRET_KEY = os.environ.get("SECRET_KEY")
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False


configuration = {
    'develop': DevConfig,
    'prod': ProdConfig
}