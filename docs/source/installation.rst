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

In version 0.2 we added Cacheing to the middleware.  By default we cache this at 15 minutes.  This can be adjusted in
your settings file by setting::

    SITE_NOTIFICATIONS_CACHE = 90

This would set your cache at 90 seconds.