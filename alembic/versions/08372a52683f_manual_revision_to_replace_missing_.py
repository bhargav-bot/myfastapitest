"""Manual revision to replace missing 12d32cad93d4

Revision ID: 08372a52683f
Revises: c99f043ee839
Create Date: 2024-06-30 22:38:11.841191

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08372a52683f'
down_revision: Union[str, None] = 'c99f043ee839'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
