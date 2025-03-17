"""merge_heads

Revision ID: 72cf2f341176
Revises: 102ac4b39c36, 2f88fb8511ef
Create Date: 2025-03-18 04:56:11.951420

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '72cf2f341176'
down_revision: Union[str, None] = ('102ac4b39c36', '2f88fb8511ef')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
