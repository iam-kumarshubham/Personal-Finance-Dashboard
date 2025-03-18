"""add columns to liabilities

Revision ID: add_columns_to_liabilities
Revises: add_timestamps_to_assets
Create Date: 2024-03-18 07:35:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'add_columns_to_liabilities'
down_revision: Union[str, None] = 'add_timestamps_to_assets'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add description, created_at, and updated_at columns to liabilities table
    op.add_column('liabilities', sa.Column('description', sa.String(), nullable=True))
    op.add_column('liabilities', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('liabilities', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))


def downgrade() -> None:
    # Remove description, created_at, and updated_at columns from liabilities table
    op.drop_column('liabilities', 'updated_at')
    op.drop_column('liabilities', 'created_at')
    op.drop_column('liabilities', 'description') 