"""add book summary

Revision ID: f0cbf8ec6ebe
Revises: 47f219fbdc76
Create Date: 2026-08-07 21:15:28.701840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0cbf8ec6ebe'
down_revision: Union[str, Sequence[str], None] = '47f219fbdc76'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "books",
        sa.Column("summary", sa.String(length=500), nullable=True)
    )

def downgrade() -> None:
    op.drop_column("books", "summary")
