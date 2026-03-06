"""Complex SQLAlchemy ORM query patterns with intentional violations."""

from sqlalchemy import select, text
from sqlalchemy.orm import Session

from models import Order, User


def orm_cte_unbounded(session: Session):
    active_users = (
        select(User.id.label("id"), User.email.label("email"))
        .where(User.active.is_(True))
        .cte("active_users")
    )

    # Intentionally no LIMIT on outer query -> VG004 expected.
    stmt = select(active_users.c.id, active_users.c.email).order_by(active_users.c.id)
    return session.execute(stmt).all()


def orm_union_all_unbounded(session: Session):
    q_active = session.query(User.id, User.email).filter(User.active.is_(True))
    q_inactive = session.query(User.id, User.email).filter(User.active.is_(False))
    # Intentionally no LIMIT on union result -> VG004 expected.
    return q_active.union_all(q_inactive).all()


def orm_left_join_unknown_filter(session: Session):
    return (
        session.query(User.id, User.email, Order.status)
        .outerjoin(Order, User.id == Order.user_id)
        .filter(text("orders.ghost_status = 'pending'"))
        .order_by(User.id)
        .limit(100)
        .all()
    )
