import os

from decouple import config
from sqlalchemy import create_engine

from api.models.model_place import Base


DB_URL = f'mysql+pymysql://root:{config("DB_PASSWORD")}@db:3306/connect?charset=utf8'
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    reset_database()
