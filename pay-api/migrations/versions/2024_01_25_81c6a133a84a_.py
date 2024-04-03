"""Script to update and correct old manually scripted migrations.

Revision ID: 81c6a133a84a
Revises: 0b1f9c35b1fb
Create Date: 2024-01-25 08:46:47.818320

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '81c6a133a84a'
down_revision = '0b1f9c35b1fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    # Generated - clean up constraint definitions
    op.drop_constraint('eft_short_names_short_name_key', 'eft_short_names', type_='unique')

    # Missing indexes
    op.create_index(op.f('ix_eft_short_names_version_auth_account_id'), 'eft_short_names_version', ['auth_account_id'], unique=False)
    op.create_index(op.f('ix_eft_short_names_version_end_transaction_id'), 'eft_short_names_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_eft_short_names_version_operation_type'), 'eft_short_names_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_eft_short_names_version_short_name'), 'eft_short_names_version', ['short_name'], unique=False)
    op.create_index(op.f('ix_eft_short_names_version_transaction_id'), 'eft_short_names_version', ['transaction_id'], unique=False)
    op.create_index(op.f('ix_eft_files_file_ref'), 'eft_files', ['file_ref'], unique=False)
    op.create_index(op.f('ix_eft_credits_payment_account_id'), 'eft_credits', ['payment_account_id'], unique=False)
    op.create_index(op.f('ix_eft_transactions_file_id'), 'eft_transactions', ['file_id'], unique=False)
    op.create_index(op.f('ix_eft_short_names_short_name'), 'eft_short_names', ['short_name'], unique=False)

    # Generated migration updates for versioning - columns should be nullable for versioning tables
    # EFT Short names version
    op.alter_column('eft_short_names_version', 'created_on',
                    existing_type=postgresql.TIMESTAMP(),
                    nullable=True,
                    autoincrement=False)
    op.alter_column('eft_short_names_version', 'short_name',
                    existing_type=sa.VARCHAR(),
                    nullable=True,
                    autoincrement=False)

    # Payment Accounts Version
    op.alter_column('payment_accounts_version', 'eft_enable',
                    existing_type=sa.BOOLEAN(),
                    nullable=True,
                    autoincrement=False,
                    existing_server_default=sa.text('false'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_eft_short_names_version_transaction_id'), table_name='eft_short_names_version')
    op.drop_index(op.f('ix_eft_short_names_version_short_name'), table_name='eft_short_names_version')
    op.drop_index(op.f('ix_eft_short_names_version_operation_type'), table_name='eft_short_names_version')
    op.drop_index(op.f('ix_eft_short_names_version_end_transaction_id'), table_name='eft_short_names_version')
    op.drop_index(op.f('ix_eft_short_names_version_auth_account_id'), table_name='eft_short_names_version')
    op.drop_index(op.f('ix_eft_files_file_ref'), table_name='eft_files')
    op.drop_index(op.f('ix_eft_credits_payment_account_id'), table_name='eft_credits')
    op.drop_index(op.f('ix_eft_transactions_file_id'), table_name='eft_transactions')
    op.drop_index(op.f('ix_eft_short_names_short_name'), table_name='eft_short_names')

    op.create_unique_constraint('eft_short_names_short_name_key', 'eft_short_names', ['short_name'])

    op.alter_column('payment_accounts_version', 'eft_enable',
                    existing_type=sa.BOOLEAN(),
                    nullable=False,
                    autoincrement=False,
                    existing_server_default=sa.text('false'))
    op.alter_column('eft_short_names_version', 'short_name',
                    existing_type=sa.VARCHAR(),
                    nullable=False,
                    autoincrement=False)
    op.alter_column('eft_short_names_version', 'created_on',
                    existing_type=postgresql.TIMESTAMP(),
                    nullable=False,
                    autoincrement=False)

    # ### end Alembic commands ###