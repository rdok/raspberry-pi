"""measurements table

Revision ID: 08f2248852a0
Revises: 
Create Date: 2020-02-15 13:34:08.114199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08f2248852a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('temperature_humidity_reading',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sensorID', sa.String(length=64), nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('takenAt', sa.DateTime(), nullable=False),
    sa.Column('temperature_c', sa.String(length=3), nullable=False),
    sa.Column('temperature_f', sa.String(length=4), nullable=False),
    sa.Column('humidity', sa.String(length=3), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_temperature_humidity_reading_createdAt'), 'temperature_humidity_reading', ['createdAt'], unique=False)
    op.create_index(op.f('ix_temperature_humidity_reading_takenAt'), 'temperature_humidity_reading', ['takenAt'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_temperature_humidity_reading_takenAt'), table_name='temperature_humidity_reading')
    op.drop_index(op.f('ix_temperature_humidity_reading_createdAt'), table_name='temperature_humidity_reading')
    op.drop_table('temperature_humidity_reading')
    # ### end Alembic commands ###