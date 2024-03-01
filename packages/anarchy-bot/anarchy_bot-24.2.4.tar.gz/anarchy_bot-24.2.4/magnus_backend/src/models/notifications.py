from enum import Enum

from tortoise import fields
from tortoise.models import Model

from entities import email, sms, telegram

from . import CreatedUpdatedModel


class Notification(Model, CreatedUpdatedModel):
    class Senders(str, Enum):
        email = email
        telegram = telegram
        sms = sms

    id = fields.IntField(pk=True)
    subject = fields.CharField(max_length=255)
    text = fields.TextField()
    user = fields.ForeignKeyField("models.User", related_name="user_notifications")
    sender = fields.CharEnumField(Senders)
    done = fields.BooleanField(default=False)

    def __str__(self):
        return self.subject
