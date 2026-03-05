"""Complex SQLAlchemy ORM query patterns (CTE, UNION, LEFT JOIN)."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Order, User


def orm_cte_active_users(session: Session):
    active_users = (
        # valk-guard:disable VG004
        select(User.id.label("id"), User.email.label("email"))
        .where(User.active.is_(True))
        .cte("active_users")
    )

    stmt = (
        select(active_users.c.id, active_users.c.email)
        .order_by(active_users.c.id)
        .limit(50)
    )
    return session.execute(stmt).all()


def orm_union_all_users(session: Session):
    # valk-guard:disable VG004
    q_active = session.query(User.id, User.email).filter(User.active.is_(True))
    # valk-guard:disable VG004
    q_inactive = session.query(User.id, User.email).filter(User.active.is_(False))
    return q_active.union_all(q_inactive).limit(100).all()


def orm_left_join_users_orders(session: Session):
    return (
        session.query(User.id, User.email, Order.status)
        .outerjoin(Order, User.id == Order.user_id)
        .filter(User.id > 0)
        .order_by(User.id)
        .limit(100)
        .all()
    )
