"""criada model associativa entre produtos e pedidos

Revision ID: d7c4c56d4ca4
Revises: 8d7301f8f025
Create Date: 2023-12-10 16:35:50.759625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7c4c56d4ca4'
down_revision: Union[str, None] = '8d7301f8f025'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_produtos_pedidos',
    sa.Column('produto_id', sa.Integer(), nullable=False),
    sa.Column('pedido_id', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pedido_id'], ['tb_pedidos.id'], ),
    sa.ForeignKeyConstraint(['produto_id'], ['tb_produtos.id'], ),
    sa.PrimaryKeyConstraint('produto_id', 'pedido_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_produtos_pedidos')
    # ### end Alembic commands ###
