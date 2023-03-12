"""empty message

Revision ID: e1ea43e0577b
Revises: 9a72d951073b
Create Date: 2023-03-12 18:49:54.019938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1ea43e0577b'
down_revision = '9a72d951073b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_name', sa.String(length=120), nullable=False),
    sa.Column('char_height', sa.Integer(), nullable=True),
    sa.Column('char_mass', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('character_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('character')
    # ### end Alembic commands ###
