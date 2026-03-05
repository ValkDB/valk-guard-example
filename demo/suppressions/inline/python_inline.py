from sqlalchemy import text
from sqlalchemy.orm import Session


def python_inline_suppression(session: Session):
    # valk-guard:disable VG001
    session.execute(text("SELECT * FROM users LIMIT 1")).all()

    session.execute(text("SELECT * FROM users LIMIT 1")).all()

    # valk-guard:disable
    session.execute(text("UPDATE users SET active = false"))
