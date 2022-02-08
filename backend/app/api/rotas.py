"""
####################################################

 ###  ##### ##### 
## ## #   #   #   
#   # #####   #   
##### #       #   
#   # #     ##### 

####################################################
"""

from flask import jsonify, request

from .. import db

from ..modelos import (
    Materia,
    Aula,
    AlunoPresencaAula,
    Usuario
)

from ..serializadores import (
    materia_schema,
    materias_schema,
    usuario_schema,
    usuarios_schema,
    aula_schema,
    aulas_schema,
    presencas_schema
)

from flask_restful import Resource


from . import api



""""""
class MateriasResource(Resource):

    def get(self):

        todas_materias = Materia.query.all()
        return jsonify(materias_schema.dump(todas_materias))

    def post(self):

        nova_materia = Materia(**request.json)
        db.session.add(nova_materia)
        db.session.commit()
        return jsonify(materia_schema.dump(nova_materia))

   
class MateriaResource(Resource):


    def get(self, materia_id):

        materia = Materia.query.get(materia_id)
        return jsonify(materia_schema.dump(materia))

    def put(self, materia_id):

        # Seleciona e edita
        materia = Materia.query.get(materia_id)
        materia.nome = request.json['nome']
        materia.emoji = request.json['emoji']
        
        # Salva e retorna
        db.session.add(materia)
        db.session.commit()
        return jsonify(materia_schema.dump(materia))

    def delete(self, materia_id):

        materia = Materia.query.get(materia_id)

        if materia:
            db.session.delete(materia)
            db.session.commit()
            return jsonify(materia_schema.dump(materia))


class ProfessoresResource(Resource):

    def get(self):
        
        todos_professores = Usuario.query.filter_by(role=1).all()
        return jsonify(usuarios_schema.dump(todos_professores))

    def post(self):

        usuario = Usuario(**request.json)
        db.session.add(usuario)
        db.session.commit()
        return jsonify(usuario_schema.dump(usuario))


class ProfessorResource(Resource):

    def get(self, professor_id):

        professor = Usuario.query.filter_by(
            id=professor_id
            ).filter_by(
            role=1
            ).first()
        
        if professor:
            return jsonify(usuario_schema.dump(professor))

    def put(self, professor_id):

        professor = Usuario.query.filter_by(
            id=professor_id
            ).first()
        
        professor.nome_usuario = request.json['nome_usuario']
        professor.nome = request.json['nome']
        professor.sobrenome = request.json['sobrenome']

        db.session.add(professor)
        db.session.commit()
        
        return jsonify(usuario_schema.dump(professor))

    def delete(self, professor_id):

        professor = Usuario.query.filter_by(
            id=professor_id
            ).first()

        if professor:
            db.session.delete(professor)
            db.session.commit()
            return jsonify(usuario_schema.dump(professor))  


class AulasResource(Resource):

    def get(self):
        todas_aulas = Aula.query.all()
        return jsonify(aulas_schema.dump(todas_aulas))

    def post(self):

        aula = Aula(**request.json)
        db.session.add(aula)
        db.session.commit()
        return jsonify(aula_schema.dump(aula))
        


class AulaResource(Resource):

    def get(self, aula_id):
        aula = Aula.query.get(aula_id)
        return jsonify(aula_schema.dump(aula))


    def put(self, aula_id):

        aula = Aula.query.get(aula_id) 

        aula.nome = request.json['nome']
        aula.professor_id = request.json['professor_id']
        aula.materia_id = request.json['materia_id']

        db.session.add(aula)
        db.session.commit()

        return jsonify(aula_schema.dump(aula))


class AlunosResource(Resource):

    def get(self):
        
        todos_alunos = Usuario.query.filter_by(role=0).all()
        return jsonify(usuarios_schema.dump(todos_alunos))

    def post(self):

        aluno = Usuario(**request.json)
        db.session.add(aluno)
        db.session.commit()
        return jsonify(usuario_schema.dump(aluno))


class AlunoResource(Resource):

    def get(self, aluno_id):
        aluno = Usuario.query.filter_by(id=aluno_id).filter_by(role=0).first()
        return jsonify(usuario_schema.dump(aluno))

    def put(self, aluno_id):

        aluno = Usuario.query.filter_by(
            id=aluno_id
            ).first()
        
        aluno.nome_usuario = request.json['nome_usuario']
        aluno.nome = request.json['nome']
        aluno.sobrenome = request.json['sobrenome']

        db.session.add(aluno)
        db.session.commit()
        return jsonify(usuario_schema.dump(aluno))

    def delete(self, aluno_id):

        aluno = Usuario.query.filter_by(
            id=aluno_id
            ).first()

        if aluno:
            db.session.delete(aluno)
            db.session.commit()
            return jsonify(usuario_schema.dump(aluno))  



class AlunosAulaResource(Resource):

    def get(self, aula_id):

        alunos_da_aula = Aula.query.get(aula_id).alunos.all()
        return jsonify(usuarios_schema.dump(alunos_da_aula))



class ListaDePresenca(Resource):

    def get(self, aula_id):

        presencas = AlunoPresencaAula.query.filter_by(
            aula_id=aula_id
            ).all()

        return jsonify(presencas_schema.dump(presencas))


    def put(self, aula_id):

        aluno_id = Usuario.query.filter_by(
            nome_usuario=request.json["nome_usuario"]
            ).first().id

        # Seleciona a presença
        presenca = AlunoPresencaAula.query.filter_by(
        aluno_id=aluno_id
        ).filter_by(
        aula_id=aula_id
        ).first()

        # Atribui o valor presente
        presenca.presente = request.json['presente']

        db.session.add(presenca)
        db.session.commit()



# Definição das rotas


# (GET) Selecionar todas as matérias
# (POST) Criar uma nova matéria
api.add_resource(MateriasResource, '/materias')

# (GET) Selecionar uma matéria
# (PUT) Editar uma matéria
# (DELETE) Apagar uma matéria
api.add_resource(MateriaResource, '/materias/<int:materia_id>')

# (GET) Selecionar todos os professores
# (POST) Criar um novo professor
api.add_resource(ProfessoresResource, '/professores')

# (GET) Selecionar um professor
# (PUT) Editar um professor
# (DELETE) Deletar um professor
api.add_resource(ProfessorResource, '/professores/<int:professor_id>')

# (GET) Selecionar todas as aulas
# (POST) Criar uma nova aula
api.add_resource(AulasResource, '/aulas')

# (GET) Selecionar uma aula
# (PUT) Editar uma aula
# (DELETE) Deletar uma aula
api.add_resource(AulaResource, '/aulas/<int:aula_id>')

# (GET) Selecionar todos os alunos
# (POST) Criar um aluno
api.add_resource(AlunosResource, '/alunos')

# (GET) Selecionar um professor
# (PUT) Editar um professor
# (DELETE) Deletar um professor
api.add_resource(AlunoResource, '/alunos/<int:aluno_id>')


# (GET) Selecionar todos os alunos de uma aula
# (POST) Vincular um aluno com uma aula
api.add_resource(AlunosAulaResource, '/aulas/<int:aula_id>/alunos')

# (PUT) Editar a presença de aluno em uma aula
api.add_resource(ListaDePresenca, '/aulas/<int:aula_id>/presenca')

