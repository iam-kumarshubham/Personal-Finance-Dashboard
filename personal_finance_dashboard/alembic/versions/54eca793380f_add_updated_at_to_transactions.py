"""add_updated_at_to_transactions

Revision ID: 54eca793380f
Revises: 066d6a9d7c29
Create Date: 2024-03-17 22:50:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = '54eca793380f'
down_revision: Union[str, None] = '066d6a9d7c29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add updated_at column to transactions table
    op.add_column('transactions', sa.Column('updated_at', sa.DateTime(timezone=True), server_default=func.now(), nullable=True))


def downgrade() -> None:
    # Remove updated_at column from transactions table
    op.drop_column('transactions', 'updated_at')
