import os
import click

from app import create_app, db

from app.modelos import (
    AlunoPresencaAula,
    Usuario,
    Aula,
    Materia
)

from flask_migrate import Migrate

from app import faker

app = create_app(os.getenv('EDUCAT_CONFIG') or 'padrao')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():

    return dict(
        db=db,
        Usuario=Usuario,
        Aula=Aula,
        Materia=Materia,
        AlunoPresencaAula=AlunoPresencaAula,
        faker=faker
    )



@app.cli.command()
def inicializar():

    print("\n\nComando click 'inicializar' chamado.\n\n")

    db.drop_all()
    db.create_all()
    faker.fakear()


@app.cli.command()
def test():
    """Execute unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)