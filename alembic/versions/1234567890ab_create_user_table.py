from alembic import op
import sqlalchemy as sa

revision = '1234567890ab'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False, unique=True)
    )

def downgrade():
    op.drop_table('users')
