"""add timestamps to assets

Revision ID: add_timestamps_to_assets
Revises: 7e4f728e3adb
Create Date: 2024-03-18 07:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'add_timestamps_to_assets'
down_revision: Union[str, None] = '7e4f728e3adb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add created_at and updated_at columns to assets table
    op.add_column('assets', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('assets', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))


def downgrade() -> None:
    # Remove created_at and updated_at columns from assets table
    op.drop_column('assets', 'updated_at')
    op.drop_column('assets', 'created_at') 