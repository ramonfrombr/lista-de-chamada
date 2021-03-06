"""empty message

Revision ID: be2c032b498f
Revises: 
Create Date: 2022-02-04 23:35:42.794119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be2c032b498f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alunos_aulas',
    sa.Column('aluno_id', sa.Integer(), nullable=True),
    sa.Column('aula_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['aluno_id'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['aula_id'], ['aulas.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alunos_aulas')
    # ### end Alembic commands ###
