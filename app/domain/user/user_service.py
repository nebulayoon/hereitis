import uuid

from app.domain.auth.auth_service import AuthService
from app.domain.user.user_exception import (
    UserExistsException,
    PasswordDoesNotMatchException,
    UserNotFoundException,
    WrongEmailorPasswordException,
)
from app.domain.user.user_model import CreateUserRequestSchema, LoginRequestSchema, User
from .user_repository import UserAlchemyRepository

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


class UserService:
    repository: UserAlchemyRepository

    def __init__(self, repository):
        self.repository = repository

    async def is_user_exists(self, email: str) -> bool:
        user = await self.repository.get_by_email(email)

        if not user:
            return False
        else:
            return True

    async def get_user(self, user_id: uuid.UUID) -> User | None:
        user = await self.repository.get_by_id(user_id)

        return user

    async def get_user_by_email(self, email: str) -> User | None:
        user = await self.repository.get_by_email(email)

        return user

    async def user_register(self, user: CreateUserRequestSchema) -> None:
        if user.password1 != user.password2:
            raise PasswordDoesNotMatchException()

        if self.is_user_exists(user.email):
            raise UserExistsException()

        hashed_password = hash_password(user.password1)

        await self.repository.save(user.name, user.email, hashed_password)

    async def login(self, login_user: LoginRequestSchema):
        user = await self.get_user_by_email(user.email)

        if not user:
            raise UserNotFoundException()

        if not verify_password(login_user.password, user.password):
            raise WrongEmailorPasswordException()

        auth_service = AuthService()
        access_token, refresh_token = await auth_service.issue_token(user_id=user.id)

        return access_token, refresh_token
