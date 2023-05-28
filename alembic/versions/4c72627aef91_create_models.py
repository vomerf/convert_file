"""create models

Revision ID: 4c72627aef91
Revises: 
Create Date: 2023-05-28 15:47:40.801357

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '4c72627aef91'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customuser',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('token', sa.String(length=36), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('record',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('path_to_record', sa.String(), nullable=False),
    sa.Column('customer_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_user_id'], ['customuser.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('record')
    op.drop_table('customuser')
    # ### end Alembic commands ###
