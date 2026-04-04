"""add content column

Revision ID: e1514af3b7c0
Revises: fdacb7ab0f95
Create Date: 2026-04-04 20:56:19.119580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1514af3b7c0'
down_revision: Union[str, Sequence[str], None] = 'fdacb7ab0f95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
