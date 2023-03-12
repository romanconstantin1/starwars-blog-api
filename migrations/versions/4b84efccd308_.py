"""empty message

Revision ID: 4b84efccd308
Revises: 02aa91a4f225
Create Date: 2023-03-12 19:23:06.528800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b84efccd308'
down_revision = '02aa91a4f225'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=120), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('gravity', sa.String(length=120), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=120), nullable=True),
    sa.Column('terrain', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('planet_name')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vehicle_name', sa.String(length=120), nullable=False),
    sa.Column('model', sa.String(length=120), nullable=True),
    sa.Column('manufacturer', sa.String(length=120), nullable=True),
    sa.Column('length', sa.String(length=120), nullable=True),
    sa.Column('crew', sa.String(length=120), nullable=True),
    sa.Column('passengers', sa.Integer(), nullable=True),
    sa.Column('mglt', sa.Integer(), nullable=True),
    sa.Column('consumables', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('vehicle_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicle')
    op.drop_table('planet')
    # ### end Alembic commands ###