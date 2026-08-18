"""baseline

Revision ID: c413588d7f60
Revises: 226a58aec7ce
Create Date: 2026-08-19 01:04:11.183841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c413588d7f60'
down_revision: Union[str, Sequence[str], None] = '226a58aec7ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
