"""fix_user_columns

Revision ID: 88258c3c4d62
Revises: e28254230fa5
Create Date: 2025-03-18 04:49:17.971052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88258c3c4d62'
down_revision: Union[str, None] = 'e28254230fa5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
