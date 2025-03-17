"""fix_password_columns

Revision ID: 102ac4b39c36
Revises: 2aebb8e752b3
Create Date: 2024-03-17 22:35:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision: str = '102ac4b39c36'
down_revision: Union[str, None] = '2aebb8e752b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create a temp table object for the update
    users = table('users',
        column('password_hash', sa.String),
        column('hashed_password', sa.String)
    )
    
    # Copy data from password_hash to hashed_password where hashed_password is null
    op.execute("""
        UPDATE users 
        SET hashed_password = password_hash 
        WHERE hashed_password IS NULL AND password_hash IS NOT NULL
    """)
    
    # Drop the password_hash column
    op.drop_column('users', 'password_hash')


def downgrade() -> None:
    # Add password_hash column
    op.add_column('users', sa.Column('password_hash', sa.String(), nullable=True))
    
    # Copy data from hashed_password to password_hash
    op.execute("""
        UPDATE users 
        SET password_hash = hashed_password 
        WHERE password_hash IS NULL AND hashed_password IS NOT NULL
    """)
