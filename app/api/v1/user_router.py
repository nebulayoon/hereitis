import uuid

from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import async_scoped_session

from app.core.config.config import config
from app.core.db.session_maker import get_db_session
from app.domain.user.user_exception import UserExistsException
from app.domain.user.user_model import (CreateUserRequestSchema,
                                        LoginRequestSchema)
from app.domain.user.user_repository import UserAlchemyRepository
from app.domain.user.user_service import UserService

user_router = APIRouter()


@user_router.post("/register")
async def register(
    request: CreateUserRequestSchema,
    session: async_scoped_session = Depends(get_db_session),
):
    repository = UserAlchemyRepository(session)
    user_service: UserService = UserService(repository)

    await user_service.user_register(request)

    return {"email": request.email, "name": request.name}


@user_router.post("/login")
async def login(
    request: LoginRequestSchema,
    response: Response,
    session: async_scoped_session = Depends(get_db_session),
):
    repository = UserAlchemyRepository(session)
    user_service: UserService = UserService(repository)

    access_token, refresh_token = await user_service.login(request)

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="Strict",
        max_age=config.ACCESS_TOKEN_EXPIRE_SECONDS,
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="Strict",
        max_age=config.REFRESH_TOKEN_EXPIRE_SECONDS,
    )

    return {"access_token": access_token, "refresh_token": refresh_token}


@user_router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")

    return {}
