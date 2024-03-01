from typing import List

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType

from core.config import config


class SingletonFastMail:
    _fast_mail_instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._fast_mail_instance, cls):
            conf = ConnectionConfig(
                MAIL_USERNAME=config.smtp_user,
                MAIL_PASSWORD=config.smtp_password,
                MAIL_FROM=config.smtp_user,
                MAIL_PORT=config.smtp_port,
                MAIL_SERVER=config.smtp_host,
                MAIL_FROM_NAME="Mangus",
                MAIL_STARTTLS=True,
                MAIL_SSL_TLS=False,
                USE_CREDENTIALS=True,
                VALIDATE_CERTS=True,
            )
            cls._fast_mail_instance = FastMail(conf)
        return cls._fast_mail_instance


async def send_mail(emails: List[str], subject, message):
    if config.is_test is False:
        message_obj = MessageSchema(
            subject=subject, recipients=emails, body=message, subtype=MessageType.html
        )
        fm = SingletonFastMail()
        await fm.send_message(message_obj)
