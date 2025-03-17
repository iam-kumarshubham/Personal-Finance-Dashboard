"""add_full_name_to_users

Revision ID: 5da91d745235
Revises: 020ff027defd
Create Date: 2024-03-17 21:49:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision: str = '5da91d745235'
down_revision: Union[str, None] = '020ff027defd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add column as nullable first
    op.add_column('users', sa.Column('full_name', sa.String(), nullable=True))
    
    # Create a temp table object for the update
    users = table('users',
        column('full_name', sa.String)
    )
    
    # Update existing records with a default value
    op.execute(users.update().values(full_name='User'))
    
    # Now make it non-nullable
    op.alter_column('users', 'full_name',
        existing_type=sa.String(),
        nullable=False
    )


def downgrade() -> None:
    op.drop_column('users', 'full_name')
