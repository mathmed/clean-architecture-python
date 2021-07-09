from sqlalchemy import Column, String, Integer, Enum
from src.infra.database.config import Base
import enum

class GenderEnum(enum.Enum):
    male = "Male"
    female = "Female"
    not_specified = "Not Specified"

class User(Base):
    """ Users Entity """
    __tablename__ = "users"

    username = Column(String(30), primary_key= True, unique=True)
    name = Column(String(30))
    last_name = Column(String(30))
    profile_image_url = Column(String, nullable=True)
    bio = Column(String(30), nullable=True)
    email = Column(String, unique=True)
    gender = Column(Enum(GenderEnum))

    def __rep__(self):
        return f"Usr [name={self.name}]"
