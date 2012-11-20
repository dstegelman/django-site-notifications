from django.contrib import messages

from site_notifications.models import Notification

class NotificationMiddleware(object):

    def process_request(self, request):
        notifications = Notification.objects.active_notifications()
        for notify in notifications:
            messages.add_message(request, notify.status, notify.message)
        return None