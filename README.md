
# Django-notifications-views
Django-notifications-views is an extension for Django-notifications-hq that provides a viewset for the notifications and expo notifications.

## Requirements
- Django >= 3.8 *
- Python >= 3.8 *
- django-notifications-hq >= 1.8 *


(*) Not tested with earlier versions.

## Quick Setup

Install package

    pip install django-notifications-views
    
Add `django_notifications_views` app to INSTALLED_APPS in your django settings.py:

```python
INSTALLED_APPS = (
    ...,
    "django.contrib.staticfiles",
	"rest_framework",  # required only if using the provided REST endpoints
    'notifications',
    'django_notifications_views',
     ...,
)
```
    
Include viewset routes

```python
from django_notifications_views.urls import router as django_notifications_views_router
your_router.registry.extend(django_notifications_views_router.registry)
```
    

### Explanation


## Contributing

-   [Juan Ignacio Borrelli](https://www.linkedin.com/in/juan-ignacio-borrelli/)
    

Maintained and developed by [Linkchar Software Development](https://linkchar.com/).


