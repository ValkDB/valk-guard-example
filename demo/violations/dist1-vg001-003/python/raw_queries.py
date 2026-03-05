from sqlalchemy import text
from sqlalchemy.orm import Session


def raw_select_star(session: Session):
    return session.execute(text("SELECT * FROM users LIMIT 1")).first()


def raw_update_without_where(session: Session):
    return session.execute(text("UPDATE users SET active = false"))


def raw_delete_without_where(session: Session):
    return session.execute(text("DELETE FROM orders"))
