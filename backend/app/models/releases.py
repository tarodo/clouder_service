from sqlalchemy import Column, ForeignKey, String, Date, UniqueConstraint
from sqlalchemy.orm import relationship
import enum
from sqlalchemy import Integer, Enum
from app.db import Base


class TryStatusEnum(str, enum.Enum):
    Start = "Start"
    Mid = "Mid"
    End = "End"


class ReleaseType(Base):
    __tablename__ = "release_type"

    id = Column(Integer, primary_key=True, index=True)
    style = Column(String, unique=True, index=True)
    base_link = Column(String, unique=True, index=True)


class ReleaseListening(Base):
    __tablename__ = "release_listening"

    id = Column(Integer, primary_key=True, index=True)
    type_id = Column(Integer, ForeignKey("release_type.id"))
    type = relationship("ReleaseType", back_populates="auditions")

    start_date = Column(Date)
    fin_date = Column(Date)

    UniqueConstraint('type_id', 'start_date', name='start_listening_block')


class ReleaseListeningTry(Base):
    __tablename__ = "release_listening_try"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(TryStatusEnum))
    date = Column(Date)
