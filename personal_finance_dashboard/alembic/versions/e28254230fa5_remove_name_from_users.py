"""remove_name_from_users

Revision ID: e28254230fa5
Revises: 8ec209c286ce
Create Date: 2024-03-17 22:20:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e28254230fa5'
down_revision: Union[str, None] = '8ec209c286ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Copy full_name to name if name exists and full_name is null
    op.execute("""
        UPDATE users 
        SET full_name = name 
        WHERE full_name IS NULL AND name IS NOT NULL
    """)
    
    # Drop the name column
    op.drop_column('users', 'name')


def downgrade() -> None:
    # Add name column back
    op.add_column('users', sa.Column('name', sa.String(), nullable=True))
    
    # Copy full_name to name
    op.execute("""
        UPDATE users 
        SET name = full_name 
        WHERE name IS NULL AND full_name IS NOT NULL
    """)
