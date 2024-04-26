from rest_framework import serializers
from users.serializers import UserSerializer
from users.models import User


class GenericNotificationRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        data = {"classname": value.__class__.__name__, "id": value.id}
        return data


class NotificationSerializer(serializers.Serializer):
    sender = UserSerializer(
        User, read_only=True
    )  # El que ejecuta el envio de la notificacion
    recipient = UserSerializer(User, read_only=True)  # El que la recibe
    unread = serializers.BooleanField(read_only=True)
    verb = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    timestamp = serializers.DateTimeField(read_only=True)
    action_object = GenericNotificationRelatedField(
        read_only=True
    )  # El elemento relacionado a la notificacion


# notify.send(actor, recipient, verb, action_object, target, level, description, public, timestamp, **kwargs)
