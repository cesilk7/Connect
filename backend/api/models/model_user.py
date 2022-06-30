from sqlalchemy import Column, Integer, String

from api.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
