"""Removed subtitles

Revision ID: 314122ce627c
Revises: b13357a90c07
Create Date: 2022-03-25 08:00:23.744683

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "314122ce627c"
down_revision = "b13357a90c07"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("blog_posts", schema=None) as batch_op:
        batch_op.drop_column("subtitle")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("blog_posts", schema=None) as batch_op:
        batch_op.drop_column("subtitle")

    # ### end Alembic commands ###
