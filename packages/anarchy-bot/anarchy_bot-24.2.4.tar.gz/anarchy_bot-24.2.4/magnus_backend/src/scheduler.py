from apscheduler.schedulers.asyncio import AsyncIOScheduler

from dao.notifications import notification_dao
from schemas.notifications import NotificationData
from utils import send_mail


async def send_notifications():
    notifications = await notification_dao.notifications()
    for notification in notifications:
        await send_mail(
            [notification.user.email], notification.subject, notification.text
        )
        notification_data = NotificationData(
            id=notification.id,
            subject=notification.subject,
            text=notification.text,
            user_id=notification.user.id,
            sender=notification.sender,
            done=True,
        )
        await notification_dao.update(notification_data)


scheduler = AsyncIOScheduler()
scheduler.add_job(send_notifications, "interval", seconds=30)
