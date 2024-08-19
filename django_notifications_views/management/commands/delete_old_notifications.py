from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from swapper import load_model

# Cargar el modelo Notification usando load_model
Notification = load_model('notifications', 'Notification')

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Verificar si la opción de autoeliminar notificaciones está habilitada en la configuración
        if not settings.DJANGO_NOTIFICATIONS_VIEWS.get('ENABLE_AUTO_DELETE_NOTIFICATIONS', False):
            self.stdout.write("Auto delete notifications is disabled.")
            return

        # Calcular la fecha umbral (notificaciones de más de 30 días)
        threshold_date = timezone.now() - timedelta(days=30)
        
        # Eliminar notificaciones antiguas
        deleted, _ = Notification.objects.filter(timestamp__lte=threshold_date).delete()
        
        # Mostrar el número de notificaciones eliminadas
        self.stdout.write(f"Deleted {deleted} old notifications.")