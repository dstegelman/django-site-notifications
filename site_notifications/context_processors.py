from django.contrib import messages
from site_notifications.models import Notification

def show_notifications(request):
    context = {}
    notifications = Notification.objects.active_notifications()
    for notify in notifications:
        messages.add_message(request, messages.INFO, notify.message)
    return context