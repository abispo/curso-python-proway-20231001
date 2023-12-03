"""empty message

Revision ID: ca2997b3864b
Revises: 2ae1f853b8a5
Create Date: 2023-12-03 15:56:36.546056

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'ca2997b3864b'
down_revision: Union[str, None] = '2ae1f853b8a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_usuarios', 'nome_usuario')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_usuarios', sa.Column('nome_usuario', mysql.VARCHAR(length=200), nullable=False))
    # ### end Alembic commands ###
