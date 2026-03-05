from sqlalchemy import text
from sqlalchemy.orm import Session


def raw_unbounded_select(session: Session):
    return session.execute(text("SELECT id, email FROM users WHERE active = true")).all()


def raw_like_leading_wildcard(session: Session):
    return session.execute(
        text("SELECT id FROM users WHERE email LIKE '%@example.com' LIMIT 1")
    ).all()


def raw_select_for_update_no_where(session: Session):
    return session.execute(text("SELECT id FROM users FOR UPDATE")).all()
