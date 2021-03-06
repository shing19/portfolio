"""item table

Revision ID: 0bd940642106
Revises: 
Create Date: 2020-02-23 23:22:09.398055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bd940642106'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('album',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('topic', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.Date(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('topic')
    )
    op.create_index(op.f('ix_album_name'), 'album', ['name'], unique=True)
    op.create_index(op.f('ix_album_timestamp'), 'album', ['timestamp'], unique=True)
    op.create_table('collection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('topic', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.Date(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('topic')
    )
    op.create_index(op.f('ix_collection_name'), 'collection', ['name'], unique=True)
    op.create_index(op.f('ix_collection_timestamp'), 'collection', ['timestamp'], unique=True)
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('topic', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.Date(), nullable=True),
    sa.Column('timespan', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('topic')
    )
    op.create_index(op.f('ix_project_name'), 'project', ['name'], unique=True)
    op.create_index(op.f('ix_project_timespan'), 'project', ['timespan'], unique=False)
    op.create_index(op.f('ix_project_timestamp'), 'project', ['timestamp'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_project_timestamp'), table_name='project')
    op.drop_index(op.f('ix_project_timespan'), table_name='project')
    op.drop_index(op.f('ix_project_name'), table_name='project')
    op.drop_table('project')
    op.drop_index(op.f('ix_collection_timestamp'), table_name='collection')
    op.drop_index(op.f('ix_collection_name'), table_name='collection')
    op.drop_table('collection')
    op.drop_index(op.f('ix_album_timestamp'), table_name='album')
    op.drop_index(op.f('ix_album_name'), table_name='album')
    op.drop_table('album')
    # ### end Alembic commands ###
