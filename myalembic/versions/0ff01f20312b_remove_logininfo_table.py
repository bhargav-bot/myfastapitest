"""Remove logininfo table

Revision ID: 0ff01f20312b
Revises: 4411e3ac9e23
Create Date: 2024-06-16 01:31:38.957884

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ff01f20312b'
down_revision: Union[str, None] = '4411e3ac9e23'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('logininfo')

  


def downgrade() -> None:
    op.create_table('logininfo',
        sa.Column('username', sa.Integer, primary_key=True, nullable=False),
        sa.Column('password', sa.String, nullable=False)
    )   
    
