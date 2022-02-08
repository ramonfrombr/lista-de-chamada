"""
####################################################

##### ##### ##### #####  ###  #     ##### #####  ###  ####  ##### ##### 
#     #     #   #   #   ## ## #       #      #  ## ## #   # #   # #   # 
##### ##### #####   #   #   # #       #     #   #   # #   # #   # ##### 
    # #     #  #    #   ##### #       #    #    ##### #   # #   # #  #  
##### ##### #   # ##### #   # ##### ##### ##### #   # ####  ##### #   # 

####################################################
"""

from . import ma



"""
####################################################

#   #  ###  ##### ##### ##### #####  ###  
## ## ## ##   #   #     #   #   #   ## ## 
# # # #   #   #   ##### #####   #   #   # 
#   # #####   #   #     #  #    #   ##### 
#   # #   #   #   ##### #   # ##### #   #  

####################################################
"""


class MateriaSchema(ma.Schema):

    # Relação Many-to-many
    aulas = ma.Nested('AulaSchema', many=True)

    class Meta:
        # Fields to expose
        fields = (
            "id",
            "nome",
            "emoji",    
            "_links")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            #"self": ma.URLFor("materia_detail", values=dict(id="<id>")),
            #"collection": ma.URLFor("materias"),
        }
    )


materia_schema = MateriaSchema()
materias_schema = MateriaSchema(many=True)


"""
####################################################

#   # ##### #   #  ###  ##### ##### ##### 
#   # #     #   # ## ## #   #   #   #   # 
#   # ##### #   # #   # #####   #   #   # 
#   #     # #   # ##### #  #    #   #   # 
##### ##### ##### #   # #   # ##### ##### 

####################################################
"""


class UsuarioSchema(ma.Schema):

    # Relação Many-to-many
    aulas = ma.Nested('AulaSchema', many=True)

    class Meta:
        # Fields to expose
        fields = (
            "id",
            "nome",
            "sobrenome",
            "nome_usuario",
            "role",
            "_links"
        )

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            #"self": ma.URLFor("usuario_detail", values=dict(id="<id>")),
            #"collection": ma.URLFor("usuarios"),
        }
    )

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)


"""
####################################################

 ###  #   # #      ###  ##### 
## ## #   # #     ## ## #     
#   # #   # #     #   # ##### 
##### #   # #     #####     # 
#   # ##### ##### #   # ##### 

####################################################
"""


class AlunoPresencaAulaSchema(ma.Schema):

    aluno = ma.Nested(UsuarioSchema, many=False)

    class Meta:
        # Fields to expose
        fields = (
            "aluno_id",
            "aula_id",
            "presente",
            "aluno"
            )

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            #"self": ma.URLFor("aula_detail", values=dict(id="<id>")),
            #"collection": ma.URLFor("aulas"),
        }
    )


presenca_schema = AlunoPresencaAulaSchema()
presencas_schema = AlunoPresencaAulaSchema(many=True)





class AulaSchema(ma.Schema):

    # Relação Many-to-many
    alunos = ma.Nested(UsuarioSchema, many=True)

    professor = ma.Nested(UsuarioSchema, many=False)

    materia = ma.Nested(MateriaSchema, many=False)

    lista_presenca = ma.Nested(AlunoPresencaAulaSchema, many=True)
    
    class Meta:
        # Fields to expose
        fields = (
            "id",
            "nome",
            "alunos",
            "professor",
            "materia",
            "lista_presenca",
            "_links")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            #"self": ma.URLFor("aula_detail", values=dict(id="<id>")),
            #"collection": ma.URLFor("aulas"),
        }
    )


aula_schema = AulaSchema()
aulas_schema = AulaSchema(many=True)


