"""LEFT JOIN demo for SQLAlchemy builder scanning."""

from sqlalchemy.orm import Session

from models import Order, User


def list_user_order_status(session: Session):
    """Return joined user/order rows with a bounded LEFT JOIN query."""
    return (
        session.query(User.id, User.email, Order.status)
        .outerjoin(Order, Order.user_id == User.id)
        .filter(User.active.is_(True))
        .limit(25)
        .all()
    )


def list_broken_user_order_status(session: Session):
    """Return a broken LEFT JOIN query that should trigger schema findings."""
    return (
        session.query(User.id, User.email, Order.ghost_status)
        .outerjoin(Order, Order.user_id == User.id)
        .filter(Order.missing_flag == "pending")
        .all()
    )
