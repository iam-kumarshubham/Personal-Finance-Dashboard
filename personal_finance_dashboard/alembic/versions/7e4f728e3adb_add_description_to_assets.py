"""add description to assets

Revision ID: 7e4f728e3adb
Revises: e517ac73fc74
Create Date: 2024-03-18 07:20:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '7e4f728e3adb'
down_revision: Union[str, None] = 'e517ac73fc74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add description column to assets table
    op.add_column('assets', sa.Column('description', sa.String(), nullable=True))


def downgrade() -> None:
    # Remove description column from assets table
    op.drop_column('assets', 'description')
