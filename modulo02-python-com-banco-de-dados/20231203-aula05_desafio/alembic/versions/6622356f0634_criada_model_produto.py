"""criada model produto

Revision ID: 6622356f0634
Revises: 82692c7156f9
Create Date: 2023-12-10 15:39:02.064585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6622356f0634'
down_revision: Union[str, None] = '82692c7156f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_produtos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sku', sa.String(length=36), nullable=False),
    sa.Column('nome', sa.String(length=200), nullable=False),
    sa.Column('descricao', sa.String(length=500), nullable=False),
    sa.Column('preco_unitario', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_produtos')
    # ### end Alembic commands ###
