import sqlalchemy as sa
from alembic import op
from sqlalchemy import table, column
from uuid import uuid4

from src.migrations.seed import get_now_str


def seed_default_plan():
    default_plan_table = table('default_plans',
                               column('id', sa.Integer),
                               column('created_date', sa.DateTime),
                               column('free_requests', sa.Integer),
                               column('cost_per_thousand_requests', sa.Integer),
                               )

    str_now = get_now_str()
    op.bulk_insert(default_plan_table,
                   [
                       {'id': uuid4(), 'created_date': op.inline_literal(str_now), 'free_requests': 5000,
                        'cost_per_thousand_requests': 1},
                   ],
                   multiinsert=False)
