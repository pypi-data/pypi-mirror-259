from pydantic import BaseModel, EmailStr, SecretStr
from datetime import date


class EmailModel(BaseModel):
    email: EmailStr


class PasswordModel(BaseModel):
    password: SecretStr


class AuthForm(EmailModel, PasswordModel):
    pass


class UserForm(BaseModel):
    firstname: str
    lastname: str
    phone_number: str


class OrganizationForm(BaseModel):
    inn: str
    ogrn: str
    org_name: str
    org_legal_address: str
    org_actual_address: str


class RegistrationForm(AuthForm, UserForm, OrganizationForm):
    pass


class EmailUpdate(PasswordModel):
    new_email: EmailStr


class PasswordUpdate(PasswordModel):
    new_password: SecretStr


class SetUsernameRequest(BaseModel):
    username: str


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    organization_id: int
    is_blocked: bool
    blocked_until_date: date | None


class JwtResponse(BaseModel):
    access_token: str
    refresh_token: str


class IsRegisteredResponse(BaseModel):
    registered: bool


class MessageResponse(BaseModel):
    message: str


class UserResponseIsBlocked(UserResponse):
    blocked_until: date


class AuthUserPayload(BaseModel):
    user_id: int


class TokenSchema(BaseModel):
    scheme: str
    credentials: str


class SetLockUserRequest(BaseModel):
    user_id: int
    days: int


class ConfirmCodeModel(BaseModel):
    code: SecretStr
