import sqlalchemy as sa
from alembic import op
from sqlalchemy import table, column

from src.migrations.seed import get_now_str, get_types_table


def seed_payment_methods():
    payment_methods_table = table('payment_methods',
                                  column('id', sa.Integer),
                                  column('method', sa.String),
                                  column('created_date', sa.DateTime))

    str_now = get_now_str()
    op.bulk_insert(payment_methods_table,
                   [
                       {'id': 1, 'method': 'Credit Card', 'created_date': op.inline_literal(str_now)},
                       {'id': 2, 'method': 'Wire Transfer', 'created_date': op.inline_literal(str_now)},
                   ],
                   multiinsert=False)


def seed_invoice_item_types():
    invoice_item_types = get_types_table('invoice_item_types')

    str_now = get_now_str()
    op.bulk_insert(invoice_item_types,
                   [
                       {'id': 1, 'type': 'Free Requests', 'created_date': op.inline_literal(str_now)},
                       {'id': 2, 'type': 'Paid Requests', 'created_date': op.inline_literal(str_now)},
                       {'id': 3, 'type': 'Discount Coupon', 'created_date': op.inline_literal(str_now)}
                   ],
                   multiinsert=False)
