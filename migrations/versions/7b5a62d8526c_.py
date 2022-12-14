"""empty message

Revision ID: 7b5a62d8526c
Revises: 7b84bef81786
Create Date: 2022-12-12 00:55:25.706049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b5a62d8526c'
down_revision = '7b84bef81786'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.alter_column('seeking_talent',
               existing_type=sa.INTEGER(),
               type_=sa.Boolean(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.alter_column('seeking_talent',
               existing_type=sa.Boolean(),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
