from django.core.management.base import BaseCommand
from django.utils import timezone
from notifications.models import Notification
from django.conf import settings
from datetime import timedelta

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        if not settings.DJANGO_NOTIFICATIONS_VIEWS.get('ENABLE_AUTO_DELETE_NOTIFICATIONS', False):
            self.stdout.write("Auto delete notifications is disabled.")
            return

        threshold_date = timezone.now() - timedelta(days=30)
        deleted, _ = Notification.objects.filter(timestamp__lte=threshold_date).delete()
        self.stdout.write(f"Deleted {deleted} old notifications.")