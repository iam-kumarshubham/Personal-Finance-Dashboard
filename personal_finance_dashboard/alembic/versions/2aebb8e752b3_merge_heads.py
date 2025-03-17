"""merge_heads

Revision ID: 2aebb8e752b3
Revises: 28c40466fb81, ed124587a2bf
Create Date: 2025-03-18 04:53:52.285623

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2aebb8e752b3'
down_revision: Union[str, None] = ('28c40466fb81', 'ed124587a2bf')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
