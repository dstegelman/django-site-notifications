from django.contrib import messages
from django.core import cache
from django.conf import settings

from site_notifications.models import Notification
from site_notifications.defaults import SITE_NOTIFICATIONS_CACHE, SITE_NOTIFICATIONS_ENABLE_CACHE


class NotificationMiddleware(object):

    def process_request(self, request):
        if getattr(settings, 'SITE_NOTIFICATIONS_ENABLE_CACHE', SITE_NOTIFICATIONS_ENABLE_CACHE):
            if not cache.get('site-notifications-notifications'):
                notifications = Notification.objects.active_notifications()
                cache.set('site-notifications-notifications', notifications, getattr(settings, 'SITE_NOTIFICATIONS_CACHE', SITE_NOTIFICATIONS_CACHE))
            else:
                notifications = cache.get('site-notifications-notifications')
        else:
            notifications = Notification.objects.active_notifications()

        for notify in notifications:
            messages.add_message(request, notify.status, notify.message)

        return None