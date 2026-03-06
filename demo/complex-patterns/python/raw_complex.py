"""Complex raw SQL execution patterns with intentional violations."""

from sqlalchemy import text
from sqlalchemy.orm import Session


def raw_cte_select_star_unbounded(session: Session):
    return session.execute(
        text(
            """
            WITH active_users AS (
                SELECT *
                FROM users
                WHERE users.active = true
            )
            SELECT active_users.id, active_users.email
            FROM active_users
            ORDER BY active_users.id
            """
        )
    ).all()


def raw_union_all_unbounded(session: Session):
    return session.execute(
        text(
            """
            SELECT users.id, users.email
            FROM users
            WHERE users.active = true
            UNION ALL
            SELECT users.id, users.email
            FROM users
            WHERE users.active = false
            """
        )
    ).all()


def raw_left_join_unknown_filter(session: Session):
    return session.execute(
        text(
            """
            SELECT users.id, users.email, orders.status
            FROM users
            LEFT JOIN orders ON users.id = orders.user_id
            WHERE orders.ghost_status = 'pending'
            ORDER BY users.id
            LIMIT 100
            """
        )
    ).all()
