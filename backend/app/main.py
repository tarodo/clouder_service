from fastapi import FastAPI

from app.api import login, users
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(login.router, tags=["login"])
app.include_router(users.router, prefix="/users", tags=["users"])
