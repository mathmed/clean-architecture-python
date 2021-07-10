from faker import Faker
from src.domain.models import User

faker = Faker()

def user_mock() -> User:
    return User(
        username= faker.name(),
        name=faker.name(),
        last_name=faker.name(),
        profile_image_url=faker.word(),
        bio=faker.word(),
        email=faker.email(),
        gender="male"
    )