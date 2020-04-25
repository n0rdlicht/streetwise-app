"""empty message

Revision ID: c7efbd46a04d
Revises: 
Create Date: 2020-04-25 16:22:08.006065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7efbd46a04d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image')
    op.drop_table('vote')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vote',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('created', sa.DATETIME(), nullable=True),
    sa.Column('updated', sa.DATETIME(), nullable=True),
    sa.Column('choice_id', sa.INTEGER(), nullable=True),
    sa.Column('other_id', sa.INTEGER(), nullable=True),
    sa.Column('is_leftimage', sa.BOOLEAN(), nullable=True),
    sa.Column('is_undecided', sa.BOOLEAN(), nullable=True),
    sa.Column('time_elapsed', sa.INTEGER(), nullable=True),
    sa.CheckConstraint('is_leftimage IN (0, 1)'),
    sa.CheckConstraint('is_undecided IN (0, 1)'),
    sa.ForeignKeyConstraint(['choice_id'], ['image.id'], ),
    sa.ForeignKeyConstraint(['other_id'], ['image.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('created', sa.DATETIME(), nullable=True),
    sa.Column('updated', sa.DATETIME(), nullable=True),
    sa.Column('Image_Key', sa.VARCHAR(length=100), nullable=True),
    sa.Column('Filename', sa.VARCHAR(length=100), nullable=True),
    sa.Column('Canton', sa.TEXT(length=10), nullable=True),
    sa.Column('Latitude', sa.FLOAT(), nullable=True),
    sa.Column('Longitude', sa.FLOAT(), nullable=True),
    sa.Column('Camera_Angle', sa.FLOAT(), nullable=True),
    sa.Column('Sequence_Key', sa.VARCHAR(length=100), nullable=True),
    sa.Column('Captured_At', sa.DATETIME(), nullable=True),
    sa.Column('Panorama', sa.BOOLEAN(), nullable=True),
    sa.CheckConstraint('"Panorama" IN (0, 1)'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
