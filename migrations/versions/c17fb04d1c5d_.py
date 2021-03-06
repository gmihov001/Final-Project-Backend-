"""empty message

Revision ID: c17fb04d1c5d
Revises: 12998328cf07
Create Date: 2020-09-02 16:42:39.442520

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c17fb04d1c5d'
down_revision = '12998328cf07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('portfolio', 'totalReturn')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portfolio', sa.Column('totalReturn', mysql.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
