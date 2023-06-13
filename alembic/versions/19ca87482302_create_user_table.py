"""create user table

Revision ID: 19ca87482302
Revises: df790dbf1c01
Create Date: 2023-06-13 12:30:52.754349

"""
from uuid import uuid4
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "19ca87482302"
down_revision = "df790dbf1c01"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.String(32),
            primary_key=True,
            default=lambda: uuid4().hex,
            index=True,
        ),
        sa.Column("email", sa.String(50), unique=True, index=True, nullable=False),
        sa.Column("password", sa.String(30), index=True, nullable=False),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("ra", sa.String(10), nullable=False, unique=True, index=True),
        sa.Column("coins", sa.Integer, nullable=False, default=0),
        sa.Column("current_level_id", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(
            ["current_level_id"],
            ["level.id"],
        ),
    )


def downgrade() -> None:
    op.drop_table("users")
