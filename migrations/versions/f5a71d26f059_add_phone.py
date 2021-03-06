"""add phone

Revision ID: f5a71d26f059
Revises: 
Create Date: 2022-03-25 13:21:22.395169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5a71d26f059'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    op.add_column('users', sa.Column('phone', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_users_phone'), 'users', ['phone'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_phone'), table_name='users')
    op.drop_column('users', 'phone')
    op.create_table('Users',

    )
    # ### end Alembic commands ###
