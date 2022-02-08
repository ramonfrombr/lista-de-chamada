# Como executar

### Cria um ambiente virtual

python -m venv venv

### Ative o ambiente virtual

. venv/bin/activate

### Instale as dependências no ambiente virtual

pip install -r requirements.txt

### Exporte as variáveis de ambiente presentes no arquivo .env

export $(cat .env | xargs)

### Ative o comando de inicialização (cria o banco de dados e preenche com informações fictícias)

flask inicializar

### Teste o aplicativo

flask test

### Ative o servidor backend

flask run

# Decisões de implementação

### flask-restful

Flask-RESTful é uma extensão para Flask que oferece suporte para construir APIs REST de maneira fácil. Esta extensão é uma leve abstração em cima das bibliotecas e ORMs de banco de dados existentes que facilita a estruturação de uma API REST completa.

### flask-marshmallow

Flask-Marshmallow é uma extensão para serialização de objetos para formato JSON que integra o Flask e a biblioteca marshmallow.

### flask-sqlalchemy

flask-
Flask-Migrate é uma extensão que lida com migrações de bancos de dados SQLAlchemy em aplicações Flask usando a ferramenta de migração Alembic. Em termos de migrações de banco de dados de fato, tudo é gerenciado pelo Alembic, sendo assim, a aplicação terá acesso a todas as funcionalidades do Alembic.

### flask-admin

Flask-Admin é uma extensão que permite criar interfaces de administrador de maneira bem fácil.