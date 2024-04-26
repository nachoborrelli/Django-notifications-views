from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushTicketError,
)
from django.conf import settings

if settings.USE_EXPO_NOTIFICATIONS:
    def send_push_message(token, message, data=None):
        """
        Send push notification to expo token associated with user.
        if token is not valid, delete it from db
        :param token: string
        :param message: string
        :param data:optional: dict
        :return: None
        """
        try:
            response = PushClient().publish(PushMessage(to=token, body=message, data=data))
        except Exception as e:
            print("Encountered push error: ", e)
        else:
            try:
                response.validate_response()

                print(response)
            except DeviceNotRegisteredError:
                from django_notifications_views.models import ExpoToken

                ExpoToken.objects.filter(token=token).delete()
            except PushTicketError as e:
                print("Encountered push error: ", e)


    def expo_push_notification_handler(recipient, verb, data, **kwargs):
        if not recipient.expo_tokens.exists():
            return

        tokens = recipient.expo_tokens.values_list("token", flat=True)
        for token in tokens:
            send_push_message(token, verb, data=data)
