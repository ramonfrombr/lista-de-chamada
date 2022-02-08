import datetime
from random import randint, choice
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db


from .modelos import (
    Usuario,
    Materia,
    Aula,
    Materia,
    AlunoPresencaAula
)


# Instância 'Faker' com linguagem definida para português-brasileiro
fake = Faker('pt_BR')



def fakear():

    materias()

    alunos()

    professores()

    aulas()

    alunos_aulas()





def materias():

    materias = [
        ('Português', '🇧🇷'),
        ('Matemática', '📊'),
        ('Biologia', '🌱'),
        ('Química', '🔥'),
        ('Física', '💡'),
        ('História', '⏳'),
        ('Geografia', '🌎'),
    ]
    
    for m, emoji in materias:

        materia = Materia(nome=m, emoji=emoji)

        db.session.add(materia)

        try:
            # Salva usuários no banco de dados
            db.session.commit()

        except IntegrityError:

            # Reverte alterações
            db.session.rollback()


def alunos(n_alunos=40):

    materias_ids = [materia.id for materia in Materia.query.all()]
  
    for i in range(n_alunos):

        nome_usuario = fake.user_name()

        # Se já ouver um aluno com o nome gerado
        if (Usuario.query.filter_by(nome_usuario=nome_usuario).first()):

            continue

        else:

            # Cria um aluno fake
            u = Usuario(
                    nome=fake.first_name(),
                    sobrenome=fake.last_name(),
                    nome_usuario=nome_usuario,
                    role=0
                )

            # Seleciona o id de uma matéria
            primeiro_id = choice(materias_ids)

            # Define uma lista de matérias sem o id selecionado
            materias_ids_secundaria = materias_ids.copy()
            materias_ids_secundaria.remove(primeiro_id)

            # Selecina o segundo id
            segundo_id = choice(materias_ids)

            # Seleciona as matérias
            materia1 = Materia.query.filter_by(id=primeiro_id).first()
            materia2 = Materia.query.filter_by(id=segundo_id).first()

            # Atribui ao usuário
            u.materias.append(materia1)
            u.materias.append(materia2)

            # Adiciona o usuário à sessão
            db.session.add(u)
        
        try:
            # Salva usuários no banco de dados
            db.session.commit()

        except IntegrityError:

            # Reverte alterações
            db.session.rollback()


def professores(n_professores=10):
    
    for i in range(n_professores):

        nome_usuario = fake.user_name()

        # Se já ouver um usuário com o nome gerado
        if (Usuario.query.filter_by(nome_usuario=nome_usuario).first()):

            continue

        else:

            # Cria um aluno fake
            u = Usuario(
                    nome=fake.first_name(),
                    sobrenome=fake.last_name(),
                    nome_usuario=nome_usuario,
                    role=1
                )

            # Adiciona o usuário à sessão
            db.session.add(u)
        
        try:
            # Salva usuários no banco de dados
            db.session.commit()

        except IntegrityError:

            # Reverte alterações
            db.session.rollback()


def aulas(n_aulas=10):

    # Seleciona todos os ids das matérias
    lista_ids_materias = [n for n in range(1, len(Materia.query.all()) + 1)]

    # Seleciona todos os ids dos professores

    professores = Usuario.query.filter_by(role=1).all()

    lista_ids_professores = []

    for p in professores:
        lista_ids_professores.append(p.id)

    
    for i in range(n_aulas):

        materia_id_escolhido = choice(lista_ids_materias)

        materia_escolhida = Materia.query.filter_by(id=materia_id_escolhido).first()

        professor_id_escolhido = choice(lista_ids_professores)

        professor_escolhido = Usuario.query.get(professor_id_escolhido)

        # Cria um aluno fake
        a = Aula(
                nome=fake.sentence(nb_words=5).capitalize(),
                materia=materia_escolhida,
                professor=professor_escolhido
            )

        # Adiciona o usuário à sessão
        db.session.add(a)
        
        try:
            # Salva usuários no banco de dados
            db.session.commit()

        except IntegrityError:

            # Reverte alterações
            db.session.rollback()


def alunos_aulas():

    # Seleciona todos os alunos
    alunos = Usuario.query.filter_by(role=0).all()

    # Para cada aluno
    for aluno in alunos:

        # Seleciona as matérias dos alunos
        materias = aluno.materias

        # Para cada matéria
        for materia in materias:

            # Para cada aula
            for aula in materia.aulas:

                # Atribui o aluno à aula da matéria
                aula.alunos.append(aluno)

                db.session.add(aula)
        
        try:
            # Salva alterações no banco de dados
            db.session.commit()

        except IntegrityError:

            # Reverte alterações
            db.session.rollback()

