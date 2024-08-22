"""empty message

Revision ID: 34393806d86c
Revises: 
Create Date: 2024-08-22 10:28:40.315397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34393806d86c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bond', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=50), nullable=False))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('bond', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###
