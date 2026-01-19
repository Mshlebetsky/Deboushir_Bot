from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from app.db.engine import Base


class User(Base):
    __tablename__ = "users"

    telegram_id = Column(BigInteger, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    accepted = Column(Integer, default=0)
    nickname = Column(String, default=None)

    posts = relationship("Posts", back_populates="user")


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.telegram_id"))
    chat_id = Column(BigInteger, nullable=False)
    message_id = Column(Integer, nullable=False)

    text = Column(String, nullable=True)  # 👈 ВАЖНО
    accepted = Column(Boolean, nullable=True)

    user = relationship("User", back_populates="posts")
