"""merge_heads

Revision ID: 8ec209c286ce
Revises: bd04de48fcc9, d5ca45eedf78
Create Date: 2025-03-18 04:08:35.452780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ec209c286ce'
down_revision: Union[str, None] = ('bd04de48fcc9', 'd5ca45eedf78')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
