from flask_admin.contrib.sqla import ModelView

from ..modelos import (
    Materia,
    Aula,
    AlunoPresencaAula,
    Usuario
)

from .. import db

from app import admin

# Interface personalizada para o modelo 'Usuario'
class ModelViewPersonalizado(ModelView):

    page_size = 50
    
    can_delete = False
    can_create = True
    can_edit = True
    can_view_details = True

    
    create_modal = True
    edit_modal = True

    column_searchable_list = ['nome']
    
    column_filters = ['sobrenome']

    column_editable_list = ['nome', 'sobrenome']


admin.add_view(ModelViewPersonalizado(Usuario, db.session, endpoint="usuarios_"))

admin.add_view(ModelView(Materia, db.session, category="Estudo", endpoint="materias_"))

admin.add_view(ModelView(Aula, db.session, category="Estudo", endpoint="aulas_"))
