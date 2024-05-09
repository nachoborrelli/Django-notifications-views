from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework import filters as rest_filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from django_filters import rest_framework as filters

from django_notifications_views.serializers import NotificationSerializer
from django_notifications_views.app_settings import api_settings as settings


class NotificationsViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
    )

    filterset_fields = ("unread",)
    
    search_fields = ("description", "verb")

    page_size_query_param = "page_size"

    ordering_fields = ("update_at", "created_at")

    serializer_class = NotificationSerializer


    def get_queryset(self):
        return self.request.user.notifications.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.unread = False
        instance.save()
        return super().retrieve(request, *args, **kwargs)

    @action(detail=False, methods=["post"], url_path="read-all")
    def mark_all_as_read(self, request):
        for notification in self.get_queryset():
            notification.unread = False
            notification.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

if settings.get_user_setting('USE_EXPO_NOTIFICATIONS'):
    from django_notifications_views.models import ExpoToken
    class ManageDeviceExpo(GenericViewSet):
        permission_classes = [IsAuthenticated]

        @action(detail=False, url_path="register-device", methods=["POST"])
        def register_device(self, request, *args, **kwargs):
            user = request.user

            token = request.data.get("token")
            if not token:
                raise ValidationError("'token' is required")

            ExpoToken.objects.update_or_create(user=user, token=token)

            # Remove oldest token if user exceeds token limit
            token_count = ExpoToken.objects.filter(user=user).count()
            if token_count > 10:
                oldest_token = ExpoToken.objects.filter(user=user).order_by("created_at").first()
                oldest_token.delete()

            return Response("token saved successfully")


        @action(detail=False, url_path="unregister-device", methods=["POST"])
        def unregister_device(self, request, *args, **kwargs):
            user = request.user

            token = request.data.get("token")
            if not token:
                raise ValidationError("token is required")

            ExpoToken.objects.filter(user=user, token=token).delete()

            return Response("token deleted successfully")