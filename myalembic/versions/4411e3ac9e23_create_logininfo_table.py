"""Create logininfo table

Revision ID: 4411e3ac9e23
Revises: 
Create Date: 2024-06-16 01:12:09.346267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4411e3ac9e23'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('logininfo')

  


def downgrade() -> None:
    op.create_table('logininfo',
        sa.Column('username', sa.Integer, primary_key=True, nullable=False),
        sa.Column('password', sa.String, nullable=False)
    )   