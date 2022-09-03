from datetime import datetime
from sqlalchemy import table, column
import sqlalchemy as sa


def seed_initial_migration():
    from src.migrations.seed.coupon_seeder import seed_coupon_discount_types, seed_coupon_recurrency_types
    seed_coupon_discount_types()
    seed_coupon_recurrency_types()

    from src.migrations.seed.payment_seeder import seed_payment_methods, seed_invoice_item_types
    seed_payment_methods()
    seed_invoice_item_types()

    from src.migrations.seed.status_seeders import seed_subscription_statuses, seed_card_statuses, \
        seed_subscription_coupon_statuses, seed_invoice_statuses, seed_coupon_statuses, \
        seed_payment_attempt_statuses
    seed_subscription_statuses()
    seed_card_statuses()
    seed_subscription_coupon_statuses()
    seed_invoice_statuses()
    seed_coupon_statuses()
    seed_payment_attempt_statuses()

    from src.migrations.seed.subscription_seeders import seed_default_plan
    seed_default_plan()


def get_types_table(table_name):
    return table(table_name,
                 column('id', sa.Integer),
                 column('type', sa.String),
                 column('created_date', sa.DateTime))


def get_statuses_table(table_name):
    return table(table_name,
                 column('id', sa.Integer),
                 column('status', sa.String),
                 column('created_date', sa.DateTime))


def get_now_str():
    now = datetime.utcnow()
    return f'{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}'
