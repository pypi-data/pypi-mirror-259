from typing import List

from models.notifications import Notification

from .general import BaseDao


class NotificationDao(BaseDao):
    async def notifications(self):
        notifications = await Notification.filter(done=False).prefetch_related("user")
        return notifications


notification_dao = NotificationDao(Notification)
