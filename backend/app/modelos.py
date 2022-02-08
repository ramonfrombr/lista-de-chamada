"""
####################################################

#   # ##### ####  ##### #     ##### ##### 
## ## #   # #   # #     #     #   # #     
# # # #   # #   # ##### #     #   # ##### 
#   # #   # #   # #     #     #   #     # 
#   # ##### ####  ##### ##### ##### ##### 

####################################################
"""


from . import db

import datetime


alunos_materias = db.Table('alunos_materias',
    db.Column('aluno_id', db.Integer, db.ForeignKey('usuarios.id')),
    db.Column('materia_id', db.Integer, db.ForeignKey('materias.id'))
)



"""
####################################################

#   #  ###  ##### ##### ##### #####  ###  
## ## ## ##   #   #     #   #   #   ## ## 
# # # #   #   #   ##### #####   #   #   # 
#   # #####   #   #     #  #    #   ##### 
#   # #   #   #   ##### #   # ##### #   #  

####################################################
"""


class Materia(db.Model):

    __tablename__ = 'materias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    emoji = db.Column(db.String(2))

    def __str__(self):
        return self.nome





"""
####################################################

#   # ##### #   #  ###  ##### ##### ##### 
#   # #     #   # ## ## #   #   #   #   # 
#   # ##### #   # #   # #####   #   #   # 
#   #     # #   # ##### #  #    #   #   # 
##### ##### ##### #   # #   # ##### ##### 

####################################################
"""


class Usuario(db.Model):

    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100))
    sobrenome = db.Column(db.String(100))
    nome_usuario = db.Column(db.String(32))


    # 0 - estudante
    # 1 - professor
    role = db.Column(db.Integer)


    materias = db.relationship(
        'Materia',
        secondary=alunos_materias,
        backref=db.backref('alunos', lazy='dynamic'),
        lazy='dynamic'
    )

    aulas = db.relationship(
        'Aula',
        secondary='alunos_presenca_aulas',
        backref=db.backref('alunos', lazy='dynamic'),
        lazy='dynamic'
    )

    @property
    def aulas_presentes(self):

        return Aula.query.join(
                AlunoPresencaAula, AlunoPresencaAula.aula_id == Aula.id
            ).filter(
                AlunoPresencaAula.aluno_id == self.id
            ).filter(
                AlunoPresencaAula.presente == 1
            )
            




"""
####################################################

 ###  #   # #      ### 
## ## #   # #     ## ##
#   # #   # #     #   #
##### #   # #     #####
#   # ##### ##### #   #

####################################################
"""


class Aula(db.Model):

    """
        id
        nome
        data
        horario
        materia_id
        professor_id
        materia
        professor
    """

    __tablename__ = 'aulas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))


    materia_id = db.Column(db.ForeignKey('materias.id'))

    professor_id = db.Column(db.ForeignKey('usuarios.id'))

    materia = db.relationship(
        'Materia',
        backref=db.backref("aulas", cascade="all, delete-orphan")
    )

    professor = db.relationship(
        'Usuario',
        backref=db.backref("aulas_lecionadas", cascade="all, delete-orphan")
    )


    def __str__(self):
        return self.nome


"""
####################################################

##### ##### ##### ##### ##### #   # #####  ###  
#   # #   # #     #     #     ##  # #     ## ## 
##### ##### ##### ##### ##### # # # #     #   # 
#     #  #  #         # #     #  ## #     ##### 
#     #   # ##### ##### ##### #   # ##### #   # 

####################################################
"""


class AlunoPresencaAula(db.Model):

    __tablename__ = 'alunos_presenca_aulas'

    aluno_id = db.Column(
        db.Integer,
        db.ForeignKey('usuarios.id'),
        primary_key=True
    )

    aula_id = db.Column(
        db.Integer,
        db.ForeignKey('aulas.id'),
        primary_key=True
    )

    aluno = db.relationship(
        'Usuario',
        backref=db.backref("lista_presenca", cascade="all, delete-orphan"))

    aula = db.relationship(
        'Aula',
        backref=db.backref("lista_presenca", cascade="all, delete-orphan"))

    # 0 - Não Definido
    # 1 - Presente
    # 2 - Ausente
    presente = db.Column(db.Integer, default=0)

