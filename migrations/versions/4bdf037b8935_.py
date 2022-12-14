"""empty message

Revision ID: 4bdf037b8935
Revises: 61fe7f1c4bb1
Create Date: 2022-12-11 22:22:30.957350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bdf037b8935'
down_revision = '61fe7f1c4bb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('website_link', sa.String(length=500), nullable=True))
        batch_op.add_column(sa.Column('looking_for_venues', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('seeking_description', sa.String(), nullable=True))

    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genres', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('website_link', sa.String(length=500), nullable=True))
        batch_op.add_column(sa.Column('looking_for_talent', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('seeking_description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.drop_column('seeking_description')
        batch_op.drop_column('looking_for_talent')
        batch_op.drop_column('website_link')
        batch_op.drop_column('genres')

    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.drop_column('seeking_description')
        batch_op.drop_column('looking_for_venues')
        batch_op.drop_column('website_link')

    op.drop_table('Show')
    # ### end Alembic commands ###
