from alembic import op
from sqlalchemy import table, column
import sqlalchemy as sa

from src.migrations.seed import get_now_str, get_types_table


def seed_coupon_discount_types():
    coupon_discount_types_table = table(
        'coupon_discount_types',
        column('id', sa.Integer),
        column('type', sa.String),
        column('order', sa.Integer),
        column('created_date', sa.DateTime))

    str_now = get_now_str()
    op.bulk_insert(coupon_discount_types_table,
                   [
                       {'id': 1, 'type': 'Literal', 'order': 0, 'created_date': op.inline_literal(str_now)},
                       {'id': 2, 'type': 'Percentage', 'order': 1, 'created_date': op.inline_literal(str_now)}
                   ],
                   multiinsert=False)


def seed_coupon_recurrency_types():
    coupon_recurrency_types_table = get_types_table('coupon_recurrency_types')

    str_now = get_now_str()
    op.bulk_insert(coupon_recurrency_types_table,
                   [
                       {'id': 1, 'type': 'One Billing Cycle', 'created_date': op.inline_literal(str_now)},
                       {'id': 2, 'type': 'Recurring', 'created_date': op.inline_literal(str_now)}
                   ],
                   multiinsert=False)
