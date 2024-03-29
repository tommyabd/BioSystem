"""empty message

Revision ID: 031f39b1ef9a
Revises: 
Create Date: 2022-05-02 00:42:16.388577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '031f39b1ef9a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    # ### end Alembic commands ###
