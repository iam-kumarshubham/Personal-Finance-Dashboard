"""fix_user_table_final

Revision ID: 066d6a9d7c29
Revises: 72cf2f341176
Create Date: 2024-03-17 22:45:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '066d6a9d7c29'
down_revision: Union[str, None] = '72cf2f341176'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop foreign key constraints first
    op.drop_constraint('assets_user_id_fkey', 'assets', type_='foreignkey')
    op.drop_constraint('liabilities_user_id_fkey', 'liabilities', type_='foreignkey')
    op.drop_constraint('transactions_user_id_fkey', 'transactions', type_='foreignkey')
    
    # Drop the existing users table
    op.drop_table('users')
    
    # Create the users table with the correct schema
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('full_name', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('is_superuser', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    
    # Recreate foreign key constraints
    op.create_foreign_key('assets_user_id_fkey', 'assets', 'users', ['user_id'], ['id'])
    op.create_foreign_key('liabilities_user_id_fkey', 'liabilities', 'users', ['user_id'], ['id'])
    op.create_foreign_key('transactions_user_id_fkey', 'transactions', 'users', ['user_id'], ['id'])


def downgrade() -> None:
    # Drop foreign key constraints first
    op.drop_constraint('assets_user_id_fkey', 'assets', type_='foreignkey')
    op.drop_constraint('liabilities_user_id_fkey', 'liabilities', type_='foreignkey')
    op.drop_constraint('transactions_user_id_fkey', 'transactions', type_='foreignkey')
    
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
