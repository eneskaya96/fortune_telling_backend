from alembic import op

from src.migrations.seed import get_now_str, get_statuses_table


def seed_subscription_statuses():
    subscription_statuses_table = get_statuses_table('subscription_statuses')

    str_now = get_now_str()
    op.bulk_insert(subscription_statuses_table,
                   [
                       {'id': 1, 'status': 'Active', 'created_date': op.inline_literal(str_now)},
                       {'id': 2, 'status': 'Expired', 'created_date': op.inline_literal(str_now)},
                       {'id': 4, 'status': 'Alerted', 'created_date': op.inline_literal(str_now)},
                       {'id': 5, 'status': 'Limited', 'created_date': op.inline_literal(str_now)},
                       {'id': 6, 'status': 'Stopped', 'created_date': op.inline_literal(str_now)}
                   ],
                   multiinsert=False)


def seed_card_statuses():
    subscription_statuses_table = get_statuses_table('card_statuses')

    str_now = get_now_str()
    op.bulk_insert(subscription_statuses_table,
                   [
                       {'id': 1, 'status': 'Default', 'created_date': op.inline_literal(str_now)},
                       {'id': 2, 'status': 'Removed', 'created_date': op.inline_literal(str_now)},
                       {'id': 3, 'status': 'Fallback', 'created_date': op.inline_literal(str_now)}
                   ],
                   multiinsert=False)


def seed_invoice_statuses():
    subscription_statuses_table = get_statuses_table('invoice_statuses')

    str_now = get_now_str()
    op.bulk_insert(subscription_statuses_table,
                   [
                       {'id': 1, 'status': 'Draft', 'created_date': op.inline_literal(str_now)},
                       {'id': 2, 'status': 'Open', 'created_date': op.inline_literal(str_now)},
                       {'id': 3, 'status': 'Paid', 'created_date': op.inline_literal(str_now)},
                       {'id': 4, 'status': 'Failed', 'created_date': op.inline_literal(str_now)},
                       {'id': 5, 'status': 'Confirm Required', 'created_date': op.inline_literal(str_now)},
                       {'id': 6, 'status': 'Deleted', 'created_date': op.inline_literal(str_now)},
                       {'id': 7, 'status': 'Waiting Open', 'created_date': op.inline_literal(str_now)}
                   ],
                   multiinsert=False)


def seed_coupon_statuses():
    coupon_statuses = get_statuses_table('coupon_statuses')
    str_now = get_now_str()
    op.bulk_insert(coupon_statuses,
                   [
                       {'id': 1, 'status': 'Valid', 'created_date': op.inline_literal(str_now)},
                       {'id': 2, 'status': 'Terminated', 'created_date': op.inline_literal(str_now)},
                       {'id': 3, 'status': 'Expired', 'created_date': op.inline_literal(str_now)},
                       {'id': 4, 'status': 'Depleted', 'created_date': op.inline_literal(str_now)}
                   ],
                   multiinsert=False)


def seed_subscription_coupon_statuses():
    subscription_coupon_statuses = get_statuses_table('subscription_coupon_statuses')
    str_now = get_now_str()
    op.bulk_insert(subscription_coupon_statuses,
                   [
                       {'id': 1, 'status': 'Active', 'created_date': op.inline_literal(str_now)},
                       {'id': 2, 'status': 'Terminated', 'created_date': op.inline_literal(str_now)},
                       {'id': 3, 'status': 'Used', 'created_date': op.inline_literal(str_now)},
                       {'id': 4, 'status': 'Cancelled', 'created_date': op.inline_literal(str_now)},
                       {'id': 5, 'status': 'Expired', 'created_date': op.inline_literal(str_now)}
                   ],
                   multiinsert=False)


def seed_payment_attempt_statuses():
    payment_attempt_statuses = get_statuses_table('payment_attempt_statuses')
    str_now = get_now_str()
    op.bulk_insert(payment_attempt_statuses,
                   [
                       {'id': 1, 'status': 'Ongoing', 'created_date': op.inline_literal(str_now)},
                       {'id': 2, 'status': 'Successful', 'created_date': op.inline_literal(str_now)},
                       {'id': 3, 'status': 'Used', 'created_date': op.inline_literal(str_now)},
                       {'id': 4, 'status': 'Action Required', 'created_date': op.inline_literal(str_now)}
                   ],
                   multiinsert=False)
