# from schemas.users import UserResponse
from tortoise.models import Model
from tortoise import fields


def is_valid_username(
    username: str
) -> bool:
    for char in username:
        if char == '_':
            continue
        if char.isalnum():
            continue
        return False
    return True


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=100, unique=True)
    password_hash = fields.CharField(max_length=128)
    firstname = fields.TextField(null=True)
    lastname = fields.TextField(null=True)
    phone_number = fields.TextField(null=True)  # if future: null=False
    username = fields.CharField(max_length=50, default='')
    is_admin = fields.BooleanField(default=False)
    blocked_until = fields.DateField(null=True, default=None)

    async def update_username(
        self,
        username: str,
    ):
        if not is_valid_username(username):
            raise ValueError('username must contain english letters and numbers only')
        if username and await self.filter(username=username):
            raise ValueError('username is not unique')
        self.username = username
        await self.save()

    async def update_email(
        self,
        email: str,
    ):
        if email and await self.filter(email=email):
            raise ValueError('email is not unique')
        self.email = email
        await self.save()

    async def update_password(
        self,
        password_hash: str,
    ):
        if password_hash is None:
            raise ValueError('password must not be None')
        self.password_hash = password_hash
        await self.save()

    def info(self) -> dict:
        return dict(
            id=self.id,
            email=self.email,
            username=self.username,
            is_blocked=bool(self.blocked_until),
            blocked_until_date=self.blocked_until,
        )


class Device(Model):
    user_agent_hash = fields.CharField(max_length=64, pk=True)
    user_agent = fields.TextField()


class ConfirmationCode(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255)
    code = fields.CharField(max_length=64)
    confirmed = fields.BooleanField(default=False)
