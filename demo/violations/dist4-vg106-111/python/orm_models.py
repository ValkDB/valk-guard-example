from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    pass


class QUser(Base):
    __tablename__ = "q_users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)


class QOrder(Base):
    __tablename__ = "q_orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)


def orm_unknown_filter_column(session: Session):
    return session.query(QUser.id).filter(text("ghost_col = 1")).limit(1).all()
