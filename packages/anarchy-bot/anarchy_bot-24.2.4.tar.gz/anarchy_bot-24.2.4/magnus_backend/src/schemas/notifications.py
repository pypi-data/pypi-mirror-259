from pydantic import BaseModel

from models.notifications import Notification


class NotificationRequest(BaseModel):
    subject: str
    text: str
    user_id: int
    sender: Notification.Senders


class NotificationData(NotificationRequest):
    id: int
    done: bool
