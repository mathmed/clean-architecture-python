import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

class DBConnectionHandler:

    def __init__(self):
        self.__connection_string = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_HOST"), os.getenv("DB_PORT"), os.getenv("DATABASE_NAME"))
        self.session = None

    def get_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close() # pylint: disable=no-member
