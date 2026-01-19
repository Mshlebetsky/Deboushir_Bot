from app.db.engine import SessionLocal
from app.db.models import User, Posts


def get_or_create_user(telegram_id: int, username: str | None):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.telegram_id == telegram_id).first()

        if not user:
            user = User(
                telegram_id=telegram_id,
                name=username,
                nickname=username
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        return user
    finally:
        db.close()



from app.db.engine import SessionLocal
from app.db.models import User, Posts


def create_post(user_id: int, chat_id: int, message_id: int):
    db = SessionLocal()
    try:
        post = Posts(
            user_id=user_id,
            chat_id=chat_id,
            message_id=message_id,
            accepted=None
        )
        db.add(post)
        db.commit()
        db.refresh(post)
        return post
    finally:
        db.close()


def get_post_by_message_id(message_id: int):
    db = SessionLocal()
    try:
        return (
            db.query(Posts)
            .filter(Posts.message_id == message_id)
            .first()
        )
    finally:
        db.close()


def get_pending_post():
    db = SessionLocal()
    try:
        post = (
            db.query(Posts)
            .options(joinedload(Posts.user))  # сразу подтягиваем user
            .filter(Posts.accepted.is_(None))
            .order_by(Posts.id)
            .first()
        )
        return post
    finally:
        db.close()




from sqlalchemy.orm import joinedload

def set_post_status(post_id: int, status: bool):
    db = SessionLocal()
    try:
        post = (
            db.query(Posts)
            .options(joinedload(Posts.user))
            .filter(Posts.id == post_id)
            .first()
        )

        if not post:
            return None

        post.accepted = status
        db.commit()
        db.refresh(post)

        return post  # ✅ ВОЗВРАЩАЕМ ORM
    finally:
        db.close()



def get_post_with_user(post_id: int):
    db = SessionLocal()
    try:
        return (
            db.query(Posts)
            .join(User)
            .filter(Posts.id == post_id)
            .first()
        )
    finally:
        db.close()