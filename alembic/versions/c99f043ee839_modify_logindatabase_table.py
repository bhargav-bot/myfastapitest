"""Modify Logindatabase table

Revision ID: c99f043ee839
Revises: 
Create Date: 2024-06-30 22:25:02.282142

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c99f043ee839'
down_revision: Union[str, None] = '12d32cad93d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('logindatabase', 'username', type_=sa.String())


def downgrade() -> None:
    op.alter_column('logindatabase', 'username', type_=sa.Integer())
