"""empty message

Revision ID: 1f09b0131153
Revises: 031f39b1ef9a
Create Date: 2022-05-02 01:33:11.735603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f09b0131153'
down_revision = '031f39b1ef9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('degerler',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('toprakNem', sa.String(), nullable=True),
    sa.Column('yagmur', sa.String(), nullable=True),
    sa.Column('isik', sa.String(), nullable=True),
    sa.Column('havaNem', sa.String(), nullable=True),
    sa.Column('havaSicaklik', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('text', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('degerler')
    # ### end Alembic commands ###
