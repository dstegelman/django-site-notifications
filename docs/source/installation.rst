============
Installation
============


To install django-site-notifications::

	pip install django-site-notifications

add to installed apps::

    INSTALLED_APPS += (
	'site_notifications',
    )

add middleware::

    'site_notifications.middleware.NotificationMiddleware',

The middleware needs to be included below the messages framework.