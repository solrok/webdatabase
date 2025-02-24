"""new Table

Revision ID: 38875c01cd75
Revises: fd5a1f8145ea
Create Date: 2024-07-26 16:30:52.248763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38875c01cd75'
down_revision = 'fd5a1f8145ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('applications',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('linkedin_url', sa.String(length=250), nullable=False),
    sa.Column('education', sa.String(length=2000), nullable=True),
    sa.Column('work_experience', sa.String(length=2000), nullable=True),
    sa.Column('resume_url', sa.String(length=500), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('applications')
    # ### end Alembic commands ###
