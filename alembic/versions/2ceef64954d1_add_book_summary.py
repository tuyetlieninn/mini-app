"""add book summary

Revision ID: 2ceef64954d1
Revises: f0cbf8ec6ebe
Create Date: 2026-08-07 21:17:23.589203

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ceef64954d1'
down_revision: Union[str, Sequence[str], None] = 'f0cbf8ec6ebe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
