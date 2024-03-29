"""model created

Revision ID: c4c22603610d
Revises: d11e4ee4adda
Create Date: 2024-02-01 16:50:36.375451

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4c22603610d'
down_revision: Union[str, None] = 'd11e4ee4adda'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('video_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'video_url')
    # ### end Alembic commands ###
