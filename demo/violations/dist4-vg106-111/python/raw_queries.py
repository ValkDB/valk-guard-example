from sqlalchemy import text
from sqlalchemy.orm import Session


def raw_unknown_filter_column(session: Session):
    return session.execute(text("SELECT q_users.id FROM q_users WHERE ghost_col = 1 LIMIT 1")).all()


def raw_unknown_table_reference(session: Session):
    return session.execute(
        text(
            "SELECT q_users.id FROM q_users "
            "INNER JOIN ghost_orders ON q_users.id = ghost_orders.user_id LIMIT 1"
        )
    ).all()


def raw_ambiguous_unqualified_column(session: Session):
    return session.execute(
        text(
            "SELECT id FROM q_users "
            "INNER JOIN q_orders ON q_users.id = q_orders.user_id LIMIT 1"
        )
    ).all()
