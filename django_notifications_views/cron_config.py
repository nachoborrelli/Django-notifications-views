from django.conf import settings
import os

# Definir el comando para ejecutar
COMMAND = "python manage.py delete_old_notifications"

# Obtener la configuración del cron desde settings del proyecto
CRON_SCHEDULE = getattr(settings, 'DJANGO_NOTIFICATIONS_VIEWS', {}).get('DJANGO_NOTIFICATIONS_CRON_SCHEDULE', '0 0 * * *')  
# Crear la línea de cron
CRON_JOB = f"{CRON_SCHEDULE} {COMMAND}"

# Guardar el cron en un archivo temporal que se pueda utilizar en la configuración del contenedor
def write_cron_job():
    cron_file_path = os.path.join(settings.BASE_DIR, "notifications_cron")
    with open(cron_file_path, "w") as cron_file:
        cron_file.write(f"{CRON_JOB}\n")
    return cron_file_path