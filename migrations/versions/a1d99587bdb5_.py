"""empty message

Revision ID: a1d99587bdb5
Revises: e1ea43e0577b
Create Date: 2023-03-12 18:50:35.555513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1d99587bdb5'
down_revision = 'e1ea43e0577b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('height', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('mass', sa.Integer(), nullable=True))
        batch_op.drop_column('char_height')
        batch_op.drop_column('char_mass')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('char_mass', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('char_height', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_column('mass')
        batch_op.drop_column('height')

    # ### end Alembic commands ###
