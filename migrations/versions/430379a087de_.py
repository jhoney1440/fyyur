"""empty message

Revision ID: 430379a087de
Revises: 9b60e4cd73a9
Create Date: 2022-12-12 07:35:50.706146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '430379a087de'
down_revision = '9b60e4cd73a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('seeking_venue', sa.String(length=11), nullable=True))
        batch_op.drop_column('looking_for_venues')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('looking_for_venues', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_column('seeking_venue')

    # ### end Alembic commands ###
