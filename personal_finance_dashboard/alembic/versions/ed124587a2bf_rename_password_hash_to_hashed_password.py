"""rename_password_hash_to_hashed_password

Revision ID: ed124587a2bf
Revises: e28254230fa5
Create Date: 2024-03-17 22:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed124587a2bf'
down_revision: Union[str, None] = 'e28254230fa5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Rename password_hash to hashed_password
    op.alter_column('users', 'password_hash',
                    new_column_name='hashed_password',
                    existing_type=sa.String(),
                    nullable=False)


def downgrade() -> None:
    # Rename hashed_password back to password_hash
    op.alter_column('users', 'hashed_password',
                    new_column_name='password_hash',
                    existing_type=sa.String(),
                    nullable=False)
