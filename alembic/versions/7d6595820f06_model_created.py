"""model created

Revision ID: 7d6595820f06
Revises: 
Create Date: 2024-01-31 17:54:07.517925

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d6595820f06'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Name', sa.String(), nullable=True),
    sa.Column('Description', sa.Text(), nullable=True),
    sa.Column('Seen', sa.Integer(), nullable=True),
    sa.Column('Posted_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('Like', sa.Integer(), nullable=True),
    sa.Column('Price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie')
    # ### end Alembic commands ###
