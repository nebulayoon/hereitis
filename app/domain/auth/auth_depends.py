from fastapi import Depends, Request, Response
from jose import JWTError

from app.domain.auth.auth_exception import NotValidateJWTTokenException
from app.domain.auth.auth_service import AuthService


async def auth_depends(
    request: Request,
    response: Response,
    auth_service: AuthService = Depends(AuthService),
):
    access_token = request.cookies.get("access_token")
    refresh_token = request.cookies.get("refresh_token")

    if access_token:
        try:
            user_id = await auth_service.decode_token(access_token)

            return user_id
        except JWTError:
            if refresh_token:
                user_id = await auth_service.decode_token(refresh_token)
                new_access_token, new_refresh_token = auth_service.issue_token(user_id)

                response.set_cookie(
                    key="access_token",
                    value=new_access_token,
                    httponly=True,
                    secure=True,
                    samesite="Strict",
                )
                response.set_cookie(
                    key="refresh_token",
                    value=new_refresh_token,
                    httponly=True,
                    secure=True,
                    samesite="Strict",
                )

            return user_id
    else:
        raise NotValidateJWTTokenException()
