from site_notifications.models import Notification
from django.contrib import messages

class NotificationMiddleware(object):

    def process_request(self, request):
        notifications = Notification.objects.active_notifications()
        for notify in notifications:
            messages.add_message(request, messages.INFO, notify.message)

        return None