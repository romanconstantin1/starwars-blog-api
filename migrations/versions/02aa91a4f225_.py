"""empty message

Revision ID: 02aa91a4f225
Revises: a1d99587bdb5
Create Date: 2023-03-12 18:53:21.631640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02aa91a4f225'
down_revision = 'a1d99587bdb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hair_color', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('skin_color', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('eye_color', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('birth_year', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('gender', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.drop_column('gender')
        batch_op.drop_column('birth_year')
        batch_op.drop_column('eye_color')
        batch_op.drop_column('skin_color')
        batch_op.drop_column('hair_color')

    # ### end Alembic commands ###
