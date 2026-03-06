from sqlalchemy import text
from sqlalchemy.orm import Session

from models import User


def orm_unbounded_select(session: Session):
    return session.query(User.id, User.email).filter(User.active.is_(True)).all()


def orm_like_leading_wildcard(session: Session):
    return session.query(User.id).filter(User.email.like("%@example.com")).limit(1).all()


def orm_select_for_update_no_where(session: Session):
    return session.execute(text("SELECT id FROM users FOR UPDATE")).all()
