"""fix_user_columns

Revision ID: 28c40466fb81
Revises: 88258c3c4d62
Create Date: 2025-03-18 04:49:32.157892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28c40466fb81'
down_revision: Union[str, None] = '88258c3c4d62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
