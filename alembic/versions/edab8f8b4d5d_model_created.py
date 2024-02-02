"""model created

Revision ID: edab8f8b4d5d
Revises: 58fbd131b0eb
Create Date: 2024-02-01 15:58:14.801504

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edab8f8b4d5d'
down_revision: Union[str, None] = '58fbd131b0eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie_video',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('video', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_video')
    # ### end Alembic commands ###