"""Complex raw SQL execution patterns (non-ORM)."""

from sqlalchemy import text
from sqlalchemy.orm import Session


def raw_cte(session: Session):
    return session.execute(
        text(
            """
            WITH active_users AS (
                SELECT users.id, users.email
                FROM users
                WHERE users.active = true
            )
            SELECT active_users.id, active_users.email
            FROM active_users
            ORDER BY active_users.id
            LIMIT 50
            """
        )
    ).all()


def raw_union_all(session: Session):
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
            LIMIT 100
            """
        )
    ).all()


def raw_left_join(session: Session):
    return session.execute(
        text(
            """
            SELECT users.id, users.email, orders.status
            FROM users
            LEFT JOIN orders ON users.id = orders.user_id
            WHERE users.id > 0
            ORDER BY users.id
            LIMIT 100
            """
        )
    ).all()
