from rest_framework.routers import DefaultRouter
from django_notifications_views.views import NotificationsViewSet


router = DefaultRouter()
router.register(r"user-notifications", NotificationsViewSet, basename="notifications")


# fmt: off
urlpatterns = [

]
# fmt: on