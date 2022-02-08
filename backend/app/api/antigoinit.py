from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource

from .. import db

from modelos import (
    Materia,
    Aula,
    AlunoPresencaAula,
    Usuario
)

from serializadores import (
    materia_schema,
    materias_schema,
    usuario_schema,
    usuarios_schema,
    aula_schema,
    aulas_schema
)

api_bp = Blueprint('api', __name__)

#api = Api(api_bp)



class MateriaResource(Resource):

    def get(self, materia_id):

        materia = Materia.query.get(materia_id)

        return jsonify(materia_schema.dump(materia))



class MateriasResource(Resource):

    def get(self):
        todas_materias = Materia.query.all()
        return jsonify(materias_schema.dump(todas_materias))

    def post(self):

        print("\n\nMétodo POST\n\n")

        print(type(request.json))

        materia = Materia(**request.json)

        db.session.add(materia)

        db.session.commit()



class AulaResource(Resource):

    def get(self, aula_id):

        print("\n\nMétodo GET\n\n")

        aula = Aula.query.get(aula_id)

        return jsonify(aula_schema.dump(aula))
        


class AulasResource(Resource):

    def get(self):

        print("\n\nMétodo GET\n\n")

        todas_aulas = Aula.query.all()

        return jsonify(aulas_schema.dump(todas_aulas))


    def post(self):

        print("\n\nMétodo POST\n\n")

        print(type(request.json))

        aula = Aula(**request.json)

        db.session.add(aula)

        db.session.commit()

        return jsonify(aula_schema.dump(aula))
        

    def put(self):
        print("\n\nMétodo PUT\n\n")
        print(request.json)


    def delete(self):
        print("\n\nMétodo DELETE\n\n")
        print(request.json)

          #db.session.delete(aula)
        #db.session.commit()



class AlunoResource(Resource):

    def get(self, aluno_id):
        aluno = Usuario.query.filter_by(id=aluno_id).filter_by(role=0).first()
        return jsonify(aula_schema.dump(aluno))


class AlunosResource(Resource):

    def get(self):
        
        todos_alunos = Usuario.query.filter_by(role=0).all()

        return jsonify(usuarios_schema.dump(todos_alunos))



class AlunosAulaResource(Resource):


    def get(self, aula_id):

        print(f"\n\nSelecionando alunos da aula #{aula_id}")

        alunos_da_aula = Aula.query.get(aula_id).alunos.all()

        print(alunos_da_aula)

        return jsonify(usuarios_schema.dump(alunos_da_aula))



class ListaDePresenca(Resource):

    def post(self, aula_id):

        lista = request.json['lista']

        for aluno in lista:
            print(aluno)
    


class ProfessorResource(Resource):

    def get(self, professor_id):

        professor = Usuario.query.filter_by(id=professor_id).filter_by(role=1).first()
        
        return jsonify(usuario_schema.dump(professor))

    def put(self, professor_id):

        professor = Usuario.query.filter_by(id=professor_id).filter_by(role=1).first()
        
        print(usuario_schema.dump(professor))


        for chave, valor in request.json.items():
            print(f"{chave}: {valor}")

        #db.session.commit()

    def delete(self, professor_id):

        professor = Usuario.query.filter_by(id=professor_id).filter_by(role=1).first()

        professor.delete()

        db.session.commit()



class ProfessoresResource(Resource):

    def get(self):
        
        todos_professores = Usuario.query.filter_by(role=1).all()

        return jsonify(usuarios_schema.dump(todos_professores))

    def post(self):

        print("\n\nMétodo POST\n\n")

        print(type(request.json))

        usuario = Usuario(**request.json)

        db.session.add(usuario)

        db.session.commit()


"""

api.add_resource(
    MateriasResource,
    '/api/materias/',
)

api.add_resource(
    MateriaResource,
    '/api/materias/<int:materia_id>/'
)

api.add_resource(
    AulasResource,
    '/api/aulas/',
)


api.add_resource(
    AulaResource,
    '/api/aulas/<int:aula_id>/'
)


api.add_resource(
    ListaDePresenca,
    '/api/aulas/<int:aula_id>/presenca/'
)


api.add_resource(
    AlunosResource,
    '/api/alunos/'
)

api.add_resource(
    AlunoResource,
    '/api/aluno/<int:aluno_id>/'
)


api.add_resource(
    AlunosAulaResource,
    '/api/aulas/<int:aula_id>/alunos/'
)


api.add_resource(
    ProfessoresResource,
    '/api/professores/'
)

api.add_resource(
    ProfessorResource,
    '/api/professores/<int:professor_id>/'
)
"""

#from . import rotas

