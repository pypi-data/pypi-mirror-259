from fastapi import Header, HTTPException, APIRouter, Depends, status
from models.users import User, Device, ConfirmationCode
from models.organizations import Organization
from typing import Annotated
import string
from random import choice
from fastapi.responses import RedirectResponse
from core.config import config
from core.security import (
    jwt_decode, ph,
    access_token_verification,
    get_token_payload,
    check_refresh_token,
    generate_jwt_tokens,
    invalidate_refresh_token,
    invalidate_user_refresh_tokens,
    invalidate_refresh_token_by_key,
    user_sessions,
    get_data_hash,
    get_current_user,
    get_current_active_user, make_confirmation_code,
    TokenType,
    crypto_user
)
from schemas.users import (
    IsRegisteredResponse,
    MessageResponse,
    RegistrationForm,
    TokenSchema,
    JwtResponse,
    EmailModel,
    AuthForm, ConfirmCodeModel,
)
from schemas.organizations import (
    # OrganizationRequest,
    OrganizationResponse
)
from services.organization import get_organization


router = APIRouter(prefix='/auth')


@router.post('/check')
async def auth_check(
    email_data: EmailModel,
) -> IsRegisteredResponse:
    '''
    check if user registered by email
    '''
    email = email_data.email
    user = await User.get_or_none(email=email)
    registered = user is not None
    return IsRegisteredResponse(registered=registered)


@router.post('/refresh')
async def refresh_tokens(refresh_token: str) -> JwtResponse:
    '''
    updates refresh_token (the old one is deleted)

    accept an active refresh token

    returns updated access and refresh tokens
    '''
    encrypt_payload = await get_token_payload(refresh_token)
    if encrypt_payload.get('token_type') != TokenType.refresh:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'refresh token invalid')
    payload = crypto_user.decrypt_data(encrypt_payload.get('encrypt', ''))
    if not await check_refresh_token(refresh_token, payload):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'refresh token not found')
    await invalidate_refresh_token(payload)
    tokens = await generate_jwt_tokens(payload)
    return tokens


@router.post('/organization')
async def get_organization_info(inn_or_ogrn: str) -> OrganizationResponse:
    '''
    returns general information about the organization
    '''
    result = get_organization(inn_or_ogrn)
    result = OrganizationResponse(**result)
    return result


@router.post('/register')
async def auth_register(
    form_data: RegistrationForm,
    user_agent: Annotated[str | None, Header()] = None
) -> JwtResponse:
    '''
    register user account

    saves the device user_agent to the shared database
    saves organization to database

    if email in config.admins_emails, then user will be an admin

    returns jwt tokens (refresh and access)
    '''
    user = await User.get_or_none(email=form_data.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail='already_registered',
        )
    password_hash = ph.hash(form_data.password.get_secret_value())
    mother_string = f"{string.ascii_letters}{string.digits}"
    username = ''.join([choice(mother_string) for _ in range(10)])
    new_user = await User.create(
        email=form_data.email,
        password_hash=password_hash,
        firstname=form_data.firstname,
        lastname=form_data.lastname,
        phone_number=form_data.phone_number,
        is_admin=form_data.email in config.admins_emails,
        username=username
    )

    user_agent_hash = get_data_hash(user_agent)
    await Device.get_or_create(
        user_agent_hash=user_agent_hash,
        user_agent=user_agent
    )
    org = await Organization.get_or_none(inn=form_data.inn)
    if org is None:
        org = Organization().update_from_dict(form_data.model_dump())
    if all([v for k, v in org if k != 'id']):
        await org.save()
        await org.users.add(new_user)
    payload = {'user_id': new_user.id, 'device': user_agent_hash}
    tokens = await generate_jwt_tokens(payload=payload)
    return tokens


@router.post('/login')
async def auth_login(
    form_data: AuthForm,
    user_agent: Annotated[str | None, Header()] = None
) -> JwtResponse:
    '''
    login user account

    return jwt tokens (refresh and access)

    if the user has been authorized before, overwrites the previous refresh_token
    '''
    exc = HTTPException(
            status_code=401,
            detail='Invalid_email_or_password'
        )
    user = await User.get_or_none(email=form_data.email)
    if not user:
        raise exc
    try:
        ph.verify(user.password_hash, form_data.password.get_secret_value())
    except:
        raise exc
    if ph.check_needs_rehash(user.password_hash):
        password_hash = ph.hash(form_data.password.get_secret_value())
        await user.update_password(
            password_hash=password_hash
        )
    user_agent_hash = get_data_hash(user_agent)
    await Device.get_or_create(
        user_agent_hash=user_agent_hash,
        user_agent=user_agent
    )
    await make_confirmation_code(form_data.email)
    payload = {'user_id': user.id, 'device': user_agent_hash}
    tokens = await generate_jwt_tokens(payload=payload)
    return tokens


@router.post('/f2a-login')
async def auth_f2a_login(
    form_data: ConfirmCodeModel,
    user_agent: Annotated[str | None, Header()] = None
) -> JwtResponse:
    '''
    login user account

    return jwt tokens
    '''
    exc = HTTPException(
            status_code=401,
            detail='Invalid_email_or_code'
        )
    confirm_code = await ConfirmationCode.filter(code=form_data.code.get_secret_value(), confirmed=False).first()

    if not confirm_code:
        raise exc

    await confirm_code.update_from_dict({'confirmed': True}).save()

    user = await User.get_or_none(email=confirm_code.email)
    if not user:
        raise exc

    user_agent_hash = get_data_hash(user_agent)
    await Device.get_or_create(
        user_agent_hash=user_agent_hash,
        user_agent=user_agent
    )
    payload = {'user_id': user.id, 'device': user_agent_hash}
    tokens = await generate_jwt_tokens(payload=payload)
    return tokens


@router.post('/logout')
async def user_logout(
    access_token: Annotated[TokenSchema, Depends(access_token_verification)],
) -> MessageResponse:
    '''
    removes refresh token from redis

    accept an access token
    '''
    encrypt_payload = await jwt_decode(access_token.credentials)
    payload = crypto_user.decrypt_data(encrypt_payload.get('encrypt', ''))
    await invalidate_refresh_token(payload)
    return MessageResponse(message='logged out successfully')


@router.post('/session/kill')
async def kill_target_session(
    token_key: str,
    access_token: Annotated[TokenSchema, Depends(access_token_verification)],
) -> MessageResponse:
    '''
    removes refresh token from redis, excluding the current one, based on the provided jwt token

    accepts a token_key in the format: `user_id_hash:device_hash`
    '''
    encrypt_payload = await jwt_decode(access_token.credentials)
    access_payload = crypto_user.decrypt_data(encrypt_payload.get('encrypt', ''))
    user_id_hash = get_data_hash(access_payload.get('user_id'))
    if f'{user_id_hash}:' not in token_key:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='token is not owned by the session user',
        )
    device_hash = access_payload.get('device')
    if f':{device_hash}' in token_key:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='current session cannot be terminated! use logout',
        )
    await invalidate_refresh_token_by_key(token_key)
    return MessageResponse(message='session is terminated')


@router.post('/session/kill/all')
async def kill_user_sessions(
    access_token: Annotated[TokenSchema, Depends(access_token_verification)],
) -> MessageResponse:
    '''
    terminate all user sessions except the current one, based on the provided JWT token
    '''
    encrypt_payload = await jwt_decode(access_token.credentials)
    access_payload = crypto_user.decrypt_data(encrypt_payload.get('encrypt', ''))
    await invalidate_user_refresh_tokens(access_payload)
    return MessageResponse(message='sessions is terminated')


@router.get('/session/list')
async def get_user_sessions(
    user: Annotated[User, Depends(get_current_user)]
):
    '''
    fetch list of user sessions
    return [user_id_hash:device_hash, ...]
    '''
    user_id_hash = get_data_hash(user.id)
    sessions = await user_sessions(user_id_hash)
    return sessions


@router.get('/test_jwt', dependencies=[Depends(get_current_active_user)])
async def test_post() -> MessageResponse:
    '''
    test jwt validation
    '''
    return MessageResponse(message='success')

