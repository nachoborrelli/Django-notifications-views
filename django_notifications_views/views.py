from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework import filters as rest_filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters

from django_notifications_views.serializers import NotificationSerializer


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