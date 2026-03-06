from sqlalchemy import text
from sqlalchemy.orm import Session


def raw_unknown_projection_column(session: Session):
    return session.execute(text("SELECT vg105_users.ghost_col FROM vg105_users LIMIT 1")).all()
