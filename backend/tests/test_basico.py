import unittest
from flask import current_app
from app.__init__ import create_app, db

class TestCaseBasico(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testes')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_aplicativo_existe(self):
        self.assertFalse(current_app is None)

    def test_aplicativo_esta_testando(self):
        self.assertTrue(current_app.config['TESTING'])