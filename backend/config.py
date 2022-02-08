import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'segredo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = 'cerulean'

    @staticmethod
    def init_app(app):
        pass


class DesenvolvimentoConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_DESENVOLVIMENTO') or \
    'sqlite:///' + os.path.join(basedir, 'dados-desenvolvimento.sqlite')


class TestesConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_TESTE') or \
    'sqlite://'


class ProducaoConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_PRODUCAO') or \
    'sqlite:///' + os.path.join(basedir, 'dados-producao.sqlite')

configuracao = {
    'desenvolvimento': DesenvolvimentoConfig,
    'testes': TestesConfig,
    'producao': ProducaoConfig,
    'padrao': DesenvolvimentoConfig
}