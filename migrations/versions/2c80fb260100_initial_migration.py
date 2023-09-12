"""initial migration

Revision ID: 2c80fb260100
Revises: e82abdde9f8c
Create Date: 2023-08-28 12:15:52.304579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c80fb260100'
down_revision = 'e82abdde9f8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_column('desvtiption')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('desvtiption', sa.VARCHAR(length=200), nullable=True))

    # ### end Alembic commands ###
