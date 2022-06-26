import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

from api.models.model_place import Base


load_dotenv()
DB_URL = f'mysql+pymysql://root:{os.environ["DB_PASSWORD"]}@db:3306/connect?charset=utf8'
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    reset_database()
