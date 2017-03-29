"""empty message

Revision ID: bc2e43a3c3ea
Revises: 0e5940f5bf43
Create Date: 2016-06-28 04:00:49.982876

"""

# revision identifiers, used by Alembic.
revision = 'bc2e43a3c3ea'
down_revision = '0e5940f5bf43'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role_invite', sa.Column('email', sa.String(), nullable=True))
    op.drop_constraint(u'role_invite_user_id_fkey', 'role_invite', type_='foreignkey')
    op.drop_column('role_invite', 'user_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role_invite', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'role_invite_user_id_fkey', 'role_invite', 'user', ['user_id'], ['id'])
    op.drop_column('role_invite', 'email')
    ### end Alembic commands ###
