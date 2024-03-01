import jwt
import core.config as config
import hashlib
import string
from random import choice

from datetime import date, datetime, timedelta
from jwt.exceptions import PyJWTError
from argon2 import PasswordHasher
from typing import Annotated, cast
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer

from schemas.users import TokenSchema, JwtResponse
from models.users import User
from db import create_redis_connection, ConfirmationCode
from utils import send_mail
from services.crypto import CryptoServer, CryptoUser


ACCESS_TOKEN_EXPIRE_MINUTES: int = 5   # put it in config
REFRESH_TOKEN_EXPIRE_MINUTES: int = 60  # put it in config


bearer_scheme = HTTPBearer()
ph = PasswordHasher()
crypto_server = CryptoServer(key_size=2048)
crypto_user = CryptoUser()


class TokenType:
    access: str = 'access'
    refresh: str = 'refresh'


def get_data_hash(data):
    data = str(data)
    f = hashlib.sha256()
    f.update(data.encode())
    return f.hexdigest()


async def create_jwt_token(data: dict, token_type: str, expire_minutes: int):
    expire = datetime.utcnow() + timedelta(minutes=expire_minutes)
    if 'exp' in data:
        data.pop('exp')
    if 'token_type' in data:
        data.pop('token_type')
    payload = {
        'encrypt': crypto_server.encrypt_data(data),
        'token_type': token_type,
        'exp': expire
    }
    return jwt.encode(
        payload,
        config.config.secret_key,
        algorithm='HS256'  # put it in config
    )


async def jwt_decode(token_credentials: str):
    try:
        payload = jwt.decode(
            token_credentials,
            config.config.secret_key,
            algorithms=['HS256']
        )
        return payload
    except jwt.exceptions.InvalidTokenError as exc:
        if isinstance(exc, jwt.exceptions.ExpiredSignatureError):
            raise HTTPException(status_code=401, detail='token is expired')
        raise HTTPException(status_code=401, detail='token is invalid')


async def get_token_credentials(token=Depends(bearer_scheme)) -> str:
    return str(token.credentials)


async def get_token_payload(token: str = Depends(get_token_credentials)):
    payload = await jwt_decode(token)
    return payload


async def create_access_token(payload: dict) -> str:
    '''creates a jwt access token'''
    return await create_jwt_token(payload, TokenType.access, ACCESS_TOKEN_EXPIRE_MINUTES)


async def create_refresh_token(payload: dict) -> str:
    '''
    creates a jwt refresh token, saving in redis with ttl:
        key = user_id_hash:device_hash,
        value=refresh_token_hash,
        expire=REFRESH_TOKEN_EXPIRE_MINUTES
    '''
    redis = await create_redis_connection()
    refresh_token = await create_jwt_token(payload, TokenType.refresh, REFRESH_TOKEN_EXPIRE_MINUTES)
    user_id_hash = get_data_hash(payload.get('user_id'))
    device_hash = payload.get('device')
    refresh_token_hash = get_data_hash(refresh_token)
    expire = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    redis.set(f'{user_id_hash}:{device_hash}', refresh_token_hash, expire)
    return refresh_token


async def generate_jwt_tokens(payload: dict) -> JwtResponse:
    access_token: str = await create_access_token(payload)
    refresh_token: str = await create_refresh_token(payload)
    return JwtResponse(access_token=access_token, refresh_token=refresh_token)


async def check_refresh_token(refresh_token: str, payload: dict) -> bool:
    redis = await create_redis_connection()
    user_id_hash = get_data_hash(payload.get('user_id'))
    device_hash = payload.get('device')
    refresh_token_hash = get_data_hash(refresh_token)
    key = f'{user_id_hash}:{device_hash}'
    value = redis.get(key)
    return value == refresh_token_hash


async def invalidate_refresh_token(payload: dict) -> None:
    '''
    invalidates a refresh token

    ?: 1. Is there a need for an additional check for availability in redis? (with check_refresh_token)
    '''
    redis = await create_redis_connection()
    user_id_hash = get_data_hash(payload.get('user_id'))
    device_hash = payload.get('device')
    key = f'{user_id_hash}:{device_hash}'
    redis.delete(key)


async def invalidate_refresh_token_by_key(token_key: str) -> None:
    '''
    invalidates a refresh token by key

    accepts a string of type: `user_id_hash:device_hash`
    '''
    redis = await create_redis_connection()
    redis.delete(token_key)


async def user_sessions(user_id_hash: str):
    redis = await create_redis_connection()
    keys = redis.keys(user_id_hash + ':*')
    return cast(list[str], keys)


async def invalidate_user_refresh_tokens(payload: dict) -> None:
    '''
    invalidates a refresh tokens except currently
    '''
    redis = await create_redis_connection()
    user_id_hash = get_data_hash(payload.get('user_id'))
    device_hash = payload.get('device')
    keys = [key for key in await user_sessions(user_id_hash) if f':{device_hash}' not in key]
    if keys:
        redis.delete(*keys)


async def invalidate_all_user_refresh_tokens(user: User) -> None:
    '''
    invalidates an all refresh tokens
    '''
    redis = await create_redis_connection()
    user_id_hash = get_data_hash(user.id)
    keys = [key for key in await user_sessions(user_id_hash)]
    if keys:
        redis.delete(*keys)


async def access_token_verification(
        token: Annotated[TokenSchema, Depends(bearer_scheme)]
) -> TokenSchema:
    '''
    validates the token type against the TokenType.access value

    returns an object of type TokenSchema if success
    '''
    payload = await jwt_decode(token.credentials)
    if payload.get('token_type') != TokenType.access:
        raise HTTPException(status_code=400, detail='access token is invalid')
    return token


async def get_current_user(
    access_token: Annotated[TokenSchema, Depends(access_token_verification)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='invalid_jwt',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = await jwt_decode(access_token.credentials)
        decr = crypto_user.decrypt_data(payload.get('encrypt', ''))
        user = await User.get_or_none(id=decr.get('user_id'))
        if user is None:
            raise credentials_exception
        return user
    except PyJWTError:
        raise credentials_exception


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.blocked_until and current_user.blocked_until > date.today():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='user_banned',
        )
    return current_user


async def get_current_active_admin_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.is_admin is False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='not_admin'
        )
    return current_user


async def make_confirmation_code(email: str):
    mother_string = "1" if config.config.is_test is True else f"{string.ascii_letters}{string.digits}"
    code = ''.join([choice(mother_string) for _ in range(6)])
    await ConfirmationCode.create(email=email, code=code)
    message = f"Your confirmation code {code}"
    await send_mail([email], "Confirmation code", message)
