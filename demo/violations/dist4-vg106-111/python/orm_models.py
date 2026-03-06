from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    pass


# Use table-shaped class names so synthetic SQL emitted from AST crawl aligns with schema tables.
class q_users(Base):
    __tablename__ = "q_users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)


class q_orders(Base):
    __tablename__ = "q_orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)


def orm_unknown_filter_column(session: Session):
    return session.query(q_users.id).filter(text("ghost_col = 1")).limit(1).all()


def orm_ambiguous_projection_column(session: Session):
    return (
        session.query(text("id"))
        .select_from(q_users)
        .join(q_orders, q_users.id == q_orders.user_id)
        .limit(1)
        .all()
    )
