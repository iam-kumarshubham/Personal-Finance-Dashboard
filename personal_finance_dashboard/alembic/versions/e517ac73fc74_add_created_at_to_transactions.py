"""add_created_at_to_transactions

Revision ID: e517ac73fc74
Revises: f0001c5b738e
Create Date: 2025-03-18 05:19:29.962787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e517ac73fc74'
down_revision: Union[str, None] = 'f0001c5b738e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
