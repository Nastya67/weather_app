import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False


config = {"dev": DevConfig,
          "prod": ProdConfig,
          "default": DevConfig}
