"""update models

Revision ID: 6d4bfa90508c
Revises: c413588d7f60
Create Date: 2026-08-19 01:08:59.236759

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d4bfa90508c'
down_revision: Union[str, Sequence[str], None] = 'c413588d7f60'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
