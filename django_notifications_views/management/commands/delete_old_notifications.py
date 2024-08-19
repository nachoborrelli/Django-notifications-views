from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from swapper import load_model

Notification = load_model('notifications', 'Notification')

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        if not settings.DJANGO_NOTIFICATIONS_VIEWS.get('AUTO_DELETE_NOTIFICATIONS', False):
            self.stdout.write("Auto delete notifications is disabled.")
            return

        threshold_date = timezone.now() - timedelta(days=30)

        # Ver cuántas notificaciones cumplen con el filtro
        notifications_to_delete = Notification.objects.filter(timestamp__lte=threshold_date)
        total_notifications = notifications_to_delete.count()

        self.stdout.write(f"Found {total_notifications} notifications to delete.")

        if total_notifications > 0:
            deleted, _ = notifications_to_delete.delete()
            self.stdout.write(f"Deleted {deleted} old notifications.")
        else:
            self.stdout.write("No notifications to delete.")