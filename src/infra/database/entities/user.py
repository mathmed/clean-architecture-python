from sqlalchemy import Column, String, Enum
from src.infra.database.config import Base
import enum

class GenderEnum(str, enum.Enum):
    male: str = "Male"
    female: str = "Female"
    not_specified: str = "Not Specified"

class User(Base):
    
    __tablename__ = "users"

    username = Column(String(30), primary_key= True, unique=True)
    name = Column(String(30))
    email = Column(String, unique=True)
    last_name = Column(String(30), nullable=True)
    profile_image_url = Column(String, nullable=True)
    bio = Column(String(30), nullable=True)
    gender = Column(Enum(GenderEnum), default="Not Specified")

    def __rep__(self):
        return f"Usr [name={self.name}]"
