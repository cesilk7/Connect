from decouple import config
from sqlalchemy import create_engine

from api.database import Base
from api.models.model_place import Place
from api.models.model_user import User
from api.models.model_visited import Visited


DB_URL = f'mysql+pymysql://root:{config("DB_PASSWORD")}@db:3306/connect?charset=utf8'
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine, tables=[
        User.__table__, Visited.__table__, Place.__table__])
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    reset_database()
