# pylint: disable=E1101
from src.infra.database.entities.user import User
from src.infra.database.config import DBConnectionHandler
from src.domain.models import User as UserModel
from src.data.contracts import UserRepositoryContract, CreateUserParams

class UserRepository(UserRepositoryContract):
    
    def insert_user(self, params: CreateUserParams) -> UserModel:
        try:
            with DBConnectionHandler() as db_connection:
                user = User(
                    username=params.username,
                    name=params.name,
                    last_name=params.last_name,
                    profile_image_url=params.profile_image_url,
                    bio=params.bio,
                    email=params.email,
                    gender=params.gender
                )
                db_connection.session.add(user)
                db_connection.session.commit()
                
                return UserModel(
                    username=user.username,
                    name=user.name,
                    last_name=user.last_name,
                    profile_image_url=user.profile_image_url,
                    bio=user.bio,
                    email=user.email,
                    gender=user.gender
                )
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
                
        return None

    def select_user(self, field_filter: str = None, value: str = None) -> UserModel:

        with DBConnectionHandler() as db_connection:
            try:
                data = db_connection.session.query(User).filter_by(**{field_filter:value}).first()
                return data
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
                
        return None