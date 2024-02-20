"""add last few column to posts table

Revision ID: e971a27262c1
Revises: 19d4726209eb
Create Date: 2024-02-20 09:35:54.896888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e971a27262c1'
down_revision: Union[str, None] = '19d4726209eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("published",sa.Boolean,nullable=False,server_default="True"))
    op.add_column("posts",sa.Column("Created_at",sa.TIMESTAMP(timezone=True),
                                  server_default=sa.text('now()'),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts","published")
    op.drop_column("posts","Created_at")
    pass
