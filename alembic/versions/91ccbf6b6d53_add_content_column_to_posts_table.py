"""add content column to posts table 

Revision ID: 91ccbf6b6d53
Revises: 96b540968240
Create Date: 2024-02-19 13:00:03.023653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '91ccbf6b6d53'
down_revision: Union[str, None] = '96b540968240'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("content",sa.String(),nullable=False),)
    pass


def downgrade() -> None:
    op.drop_column("posts","content")
    pass
