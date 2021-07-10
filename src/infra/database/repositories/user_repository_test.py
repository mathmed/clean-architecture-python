from faker import Faker
from src.infra.database.config import DBConnectionHandler
from src.data.contracts import CreateUserParams
from .user_repository import UserRepository


faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()

def test_insert_and_select_user():
    """Should insert and select correctly user"""
    username= faker.name()
    name=faker.name()
    last_name=faker.name()
    profile_image_url=faker.word()
    bio=faker.word()
    email=faker.email()
    gender="male"

    engine = db_connection_handler.get_engine()

    user = user_repository.insert_user(CreateUserParams(username, name, email, last_name, profile_image_url, bio, gender))
    select_user = user_repository.select_user("username", username)

    assert user.username == select_user.username
    assert user.name == select_user.name
    assert user.last_name == select_user.last_name
    assert user.profile_image_url == select_user.profile_image_url
    assert user.bio == select_user.bio
    assert user.email == select_user.email
    assert user.gender == select_user.gender

    engine.execute("DELETE FROM users WHERE username = '{}';".format(user.username))

