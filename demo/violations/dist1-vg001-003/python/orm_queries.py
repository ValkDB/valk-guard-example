from sqlalchemy.orm import Session

from models import Order, User


def orm_recent_user(session: Session):
    return session.query(User.id, User.email).filter(User.active.is_(True)).limit(1).all()


def orm_update_without_where(session: Session):
    return session.query(User).update({"active": False})


def orm_delete_without_where(session: Session):
    return session.query(Order).delete()
