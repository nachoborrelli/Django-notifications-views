from rest_framework.routers import DefaultRouter
from django_notifications_views.views import NotificationsViewSet
from django_notifications_views.app_settings import api_settings as settings


router = DefaultRouter()
router.register(r"user-notifications", NotificationsViewSet, basename="notifications")

if settings.get_user_setting("USE_EXPO_NOTIFICATIONS"):
    from django_notifications_views.views import ManageDeviceExpo
    router.register(r"expo-devices", ManageDeviceExpo, basename="expo")
