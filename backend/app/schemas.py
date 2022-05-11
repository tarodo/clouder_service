from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    full_name: str | None
    email: str | None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    disabled: bool = False

    class Config:
        orm_mode = True