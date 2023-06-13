"""create level table

Revision ID: df790dbf1c01
Revises: 
Create Date: 2023-06-12 19:46:12.447938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df790dbf1c01'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'level',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('question', sa.String(250), nullable=False),
        sa.Column('right_answer', sa.String(250), nullable=False),
        sa.Column('reward', sa.Integer, nullable=False),
        sa.Column('wrong_answer_1', sa.String(250), nullable=False),
        sa.Column('wrong_answer_2', sa.String(250), nullable=False),
        sa.Column('wrong_answer_3', sa.String(250), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('level')
