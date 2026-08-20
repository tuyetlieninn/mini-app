from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.core.security import hash_password, verify_password, create_access_token

def list_users(db: Session) -> list[UserRead]:
    users = db.query(User).order_by(User.id).all()
    return [UserRead.model_validate(u) for u in users]

def get_user(db: Session, user_id: int) -> UserRead:
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserRead.model_validate(user)

def create_user(db: Session, payload: UserCreate) -> UserRead:
    if db.query(User).filter(User.username == payload.username).first():
        raise HTTPException(status_code=409, detail="Username already exists")

    user = User(
        username=payload.username,
        hashed_password=hash_password(payload.password),
        role=payload.role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserRead.model_validate(user)

def update_user(db: Session, user_id: int, payload: UserUpdate) -> UserRead:
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if payload.username:
        existing = db.query(User).filter(User.username == payload.username).first()
        if existing and existing.id != user_id:
            raise HTTPException(status_code=409, detail="Username already exists")
    update_data = payload.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        if field == "password":
            value = hash_password(value)
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return UserRead.model_validate(user)

def delete_user(db: Session, user_id: int) -> None:
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    
def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()


def login(db: Session, username: str, password: str) -> str:
    user = get_user_by_username(db, username)

    if user is None or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    return create_access_token(user.username)