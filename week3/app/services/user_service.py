from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.core.security import hash_password

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
        if db.query(User).filter(User.username == payload.username).first():
            raise HTTPException(status_code=409, detail="Username already exists")
        user.username = payload.username

    if payload.password:
        user.hashed_password = hash_password(payload.password)

    if payload.role is not None:
        user.role = payload.role

    db.commit()
    db.refresh(user)
    return UserRead.model_validate(user)

def delete_user(db: Session, user_id: int) -> None:
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
