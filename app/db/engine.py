from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from app.config import DB_LITE
from sqlalchemy import (
    String,
    Text,
    DateTime,
    func,
    Boolean,
    Integer,
    BigInteger,
)

engine = create_engine(
    DB_LITE,
    echo=False,  # True — если хочешь видеть SQL-запросы в консоли
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

class Base(DeclarativeBase):

    __abstract__ = True

    created: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )
