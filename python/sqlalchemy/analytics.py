"""Analytics service with SQLAlchemy ORM queries.

Clean queries — no anti-patterns in main branch.
"""

from sqlalchemy import text
from sqlalchemy.orm import Session

from models import Order, User


def get_user_by_id(session: Session, user_id: int):
    """Retrieve a single user by ID."""
    return (
        session.query(User.id, User.email, User.name, User.active)
        .filter(User.id == user_id)
        .limit(1)
        .first()
    )


def get_recent_orders(session: Session, limit: int = 50):
    """Retrieve recent pending orders with a limit."""
    return (
        session.query(Order.id, Order.user_id, Order.status, Order.total, Order.created_at)
        .filter(Order.status == "pending")
        .order_by(Order.created_at.desc())
        .limit(limit)
        .all()
    )


def get_active_users(session: Session, limit: int = 100):
    """Retrieve active users with a limit."""
    return (
        session.query(User.id, User.email, User.name, User.active, User.created_at)
        .filter(User.active.is_(True))
        .order_by(User.created_at.desc())
        .limit(limit)
        .all()
    )


def get_user_snapshot_raw(session: Session):
    """Retrieve one user using SQLAlchemy text()/execute() path."""
    return session.execute(
        text("SELECT id, email, name, active FROM users WHERE id = 1 LIMIT 1"),
    ).first()
