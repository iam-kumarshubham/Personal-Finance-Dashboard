"""add_updated_at_to_users

Revision ID: bd04de48fcc9
Revises: d5ca45eedf77
Create Date: 2025-03-18 04:06:15.058084

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd04de48fcc9'
down_revision: Union[str, None] = 'd5ca45eedf77'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
