from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class VG101User(Base):
    __tablename__ = "vg101_users"

    id = Column(Integer, primary_key=True)
    ghost_col = Column(String(64))


class VG102Account(Base):
    __tablename__ = "vg102_accounts"

    id = Column(Integer, primary_key=True)


class VG103Order(Base):
    __tablename__ = "vg103_orders"

    id = Column(Integer, primary_key=True)
    total = Column(String(32))


class VG104AuditEvent(Base):
    __tablename__ = "vg104_audit_events"

    id = Column(Integer, primary_key=True)
