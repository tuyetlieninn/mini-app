"""add book summary

Revision ID: 47f219fbdc76
Revises: da64614cd343
Create Date: 2026-08-07 21:09:16.894996

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47f219fbdc76'
down_revision: Union[str, Sequence[str], None] = 'da64614cd343'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "books",
        sa.Column("summary", sa.String(length=500), nullable=True)
    )

def downgrade() -> None:
    op.drop_column("books", "summary")
