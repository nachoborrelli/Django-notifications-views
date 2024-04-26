from django.conf import settings

USER_SETTINGS = getattr(settings, "DJANGO_NOTIFICATIONS_VIEWS", None)

DEFAULTS = {
    'USE_EXPO_NOTIFICATIONS': False,
    'EXPO_APP_ID': '', 
}

class APISettings:
    def __init__(self, user_settings=None, defaults=None):
        self.defaults = defaults
        self._user_settings = self.__check_user_settings(user_settings) \
            if user_settings else {}

    def __check_user_settings(self, user_settings):
        for setting in user_settings:
            if setting not in self.defaults:
                raise RuntimeError(f"The {setting} setting is not a valid setting for DJANGO_NOTIFICATIONS_VIEWS.")

        return user_settings

    def get_user_setting(self, attr):
        try:
            return self._user_settings[attr]
        except KeyError:
            return self.defaults[attr]


api_settings = APISettings(USER_SETTINGS, DEFAULTS)


