"""empty message

Revision ID: 9c34906d047f
Revises: 7f20ed7b232a
Create Date: 2017-07-18 12:42:42.454032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c34906d047f'
down_revision = '7f20ed7b232a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('deleted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog', 'deleted')
    # ### end Alembic commands ###
