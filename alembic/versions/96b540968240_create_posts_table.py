"""create posts  table

Revision ID: 96b540968240
Revises: 
Create Date: 2024-02-19 12:43:35.517532

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96b540968240'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts",sa.Column("id",sa.Integer(),nullable=False,primary_key=True),sa.Column("title",sa.String,nullable=False))
    pass

def downgrade() -> None:
    op.drop_table("posts")
    pass
