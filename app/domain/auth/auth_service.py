from jose import JWTError, jwt
from datetime import datetime, timezone
from app.core.config.config import config
from app.domain.auth.auth_exception import NotValidateJWTTokenException


class AuthService:
    async def create_token(self, data: dict, expires_delta: int):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + (expires_delta)
        to_encode.update({"exp": expire})

        return jwt.encode(to_encode, config.SECRET_KEY, algorithm="HS256")

    async def issue_token(self, user_id: str):
        payload = {"sub": user_id}
        access_token = await self.create_token(
            payload, expires_delta=config.ACCESS_TOKEN_EXPIRE_SECONDS
        )

        refresh_token = await self.create_token(
            {"sub": user_id, "refresh": "refresh"}, config.REFRESH_TOKEN_EXPIRE_SECONDS
        )

        return access_token, refresh_token

    def decode_token(token: str):
        try:
            payload = jwt.decode(token, config.SECRET_KEY, algorithms="HS256")
            user_id = payload.get("sub")

            if user_id is None:
                raise NotValidateJWTTokenException()

            return user_id
        except JWTError:
            raise NotValidateJWTTokenException()
