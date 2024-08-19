from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from swapper import load_model

Notification = load_model('notifications', 'Notification')

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        app_settings = getattr(settings, 'DJANGO_NOTIFICATIONS_VIEWS', {})
        auto_delete = app_settings.get('AUTO_DELETE_NOTIFICATIONS', False)
        delete_days = app_settings.get('NOTIFICATIONS_DELETE_DAYS', 30)  

        if not auto_delete:
            self.stdout.write("Auto delete notifications is disabled.")
            return

        threshold_date = timezone.now() - timedelta(days=delete_days)

        notifications_to_delete = Notification.objects.filter(timestamp__lte=threshold_date)
        total_notifications = notifications_to_delete.count()

        if total_notifications > 0:
            deleted, _ = notifications_to_delete.delete()
            self.stdout.write(f"Deleted {deleted} old notifications.")
        else:
            self.stdout.write("No notifications to delete.")