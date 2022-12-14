"""Initial migration

Revision ID: 7e7fdd2796ac
Revises: 
Create Date: 2022-08-25 14:22:14.339560+00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.

revision = '7e7fdd2796ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fortune',
                    sa.Column('id', sa.String(length=36), nullable=False),
                    sa.Column('created_date', sa.DateTime(), nullable=False),
                    sa.Column('modified_date', sa.DateTime(), nullable=True),
                    sa.Column('fortune', sa.String(length=250), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_fortune_fortune'), 'fortune', ['fortune'], unique=True)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_fortune_fortune'), table_name='fortune')
    op.drop_table('fortune')

    # ### end Alembic commands ###
