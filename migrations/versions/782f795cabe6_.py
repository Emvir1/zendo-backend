"""empty message

Revision ID: 782f795cabe6
Revises: 26cc31ffd388
Create Date: 2026-04-09 12:30:22.853700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '782f795cabe6'
down_revision = '26cc31ffd388'
branch_labels = None
depends_on = None


def upgrade():
    # Fix list_id in tasks to be nullable (matches model definition)
    op.alter_column('tasks', 'list_id',
                    existing_type=sa.INTEGER(),
                    nullable=True)


def downgrade():
    op.alter_column('tasks', 'list_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
