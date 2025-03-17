"""add_user_status_columns

Revision ID: d5ca45eedf77
Revises: dc0f579796cf
Create Date: 2024-03-17 22:05:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision: str = 'd5ca45eedf77'
down_revision: Union[str, None] = 'dc0f579796cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add is_active column
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    
    # Add is_superuser column
    op.add_column('users', sa.Column('is_superuser', sa.Boolean(), nullable=True))
    
    # Create a temp table object for the update
    users = table('users',
        column('is_active', sa.Boolean),
        column('is_superuser', sa.Boolean)
    )
    
    # Update existing records with default values
    op.execute(users.update().values(
        is_active=True,
        is_superuser=False
    ))
    
    # Make columns non-nullable
    op.alter_column('users', 'is_active',
        existing_type=sa.Boolean(),
        nullable=False
    )
    op.alter_column('users', 'is_superuser',
        existing_type=sa.Boolean(),
        nullable=False
    )


def downgrade() -> None:
    op.drop_column('users', 'is_superuser')
    op.drop_column('users', 'is_active')
