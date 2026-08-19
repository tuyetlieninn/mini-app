from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: int = 1

class UserRead(BaseModel):
    id: int
    username: str
    role: int

    model_config = {"from_attributes": True}

class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    role: int | None = None
