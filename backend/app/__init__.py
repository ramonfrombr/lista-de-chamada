from flask import Flask

from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView

from config import configuracao


# Inicia as extensões (sem vinculá-las ao aplicativo, assim poderão ser corretamente importadas dentro dos módulos)
mail = Mail()
db = SQLAlchemy()
ma = Marshmallow()
admin = Admin()
migrate = Migrate()
admin = Admin(name='EduCAT', template_mode='bootstrap3')


def create_app(nome_configuracao):

    # Cria e configura o aplicativo
    app = Flask(__name__)
    app.config.from_object(configuracao[nome_configuracao])
    configuracao[nome_configuracao].init_app(app)
    
    # Vincula as extensões ao aplicativo
    mail.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    admin.init_app(app)

    # 
    from flask_cors import CORS
    CORS(app)

    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    # A extensão API é importada dentro do Blueprint
    # Prefixando o blueprint com 'api' evita que cada rota tenha de ter prefixada individualmente
    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')


    return app