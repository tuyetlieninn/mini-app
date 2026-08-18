"""baseline

Revision ID: 226a58aec7ce
Revises: 37acfb347e44
Create Date: 2026-08-19 01:03:53.654898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '226a58aec7ce'
down_revision: Union[str, Sequence[str], None] = '37acfb347e44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
