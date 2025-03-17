"""add_hashed_password_to_users

Revision ID: dc0f579796cf
Revises: 5da91d745235
Create Date: 2024-03-17 22:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision: str = 'dc0f579796cf'
down_revision: Union[str, None] = '5da91d745235'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add column as nullable first
    op.add_column('users', sa.Column('hashed_password', sa.String(), nullable=True))
    
    # Create a temp table object for the update
    users = table('users',
        column('hashed_password', sa.String)
    )
    
    # Update existing records with a default hashed password
    # This is a temporary value that should be changed by users
    op.execute(users.update().values(hashed_password='$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj1ZxQQxq3re'))
    
    # Now make it non-nullable
    op.alter_column('users', 'hashed_password',
        existing_type=sa.String(),
        nullable=False
    )


def downgrade() -> None:
    op.drop_column('users', 'hashed_password')
