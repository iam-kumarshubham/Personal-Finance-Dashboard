"""add_updated_at_to_users

Revision ID: d5ca45eedf78
Revises: d5ca45eedf77
Create Date: 2024-03-17 22:10:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision: str = 'd5ca45eedf78'
down_revision: Union[str, None] = 'd5ca45eedf77'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add updated_at column
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), nullable=True))
    
    # Create a temp table object for the update
    users = table('users',
        column('updated_at', sa.DateTime)
    )
    
    # Update existing records with current timestamp
    op.execute(users.update().values(
        updated_at=sa.func.now()
    ))
    
    # Make column non-nullable
    op.alter_column('users', 'updated_at',
        existing_type=sa.DateTime(),
        nullable=False
    )


def downgrade() -> None:
    op.drop_column('users', 'updated_at') 