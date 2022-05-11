from sqlalchemy import Boolean, Column, Integer, String

from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String, index=True, default="")
    email = Column(String, index=True, default="")
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)
