"""add_created_at_to_transactions

Revision ID: f0001c5b738e
Revises: 54eca793380f
Create Date: 2024-03-17 22:55:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = 'f0001c5b738e'
down_revision: Union[str, None] = '54eca793380f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add created_at column to transactions table
    op.add_column('transactions', sa.Column('created_at', sa.DateTime(timezone=True), server_default=func.now(), nullable=False))


def downgrade() -> None:
    # Remove created_at column from transactions table
    op.drop_column('transactions', 'created_at')
