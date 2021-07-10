import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

class DBConnectionHandler:

    def __init__(self):
        self.__connection_string = "mysql+pymysql://{}:{}@{}:3306/{}?charset=utf8mb4".format(os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("MYSQL_HOST"), os.getenv("MYSQL_DATABASE"))
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
