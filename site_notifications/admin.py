from django.contrib import admin

from site_notifications.models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'start_date', 'end_date', 'enabled')

admin.site.register(Notification, NotificationAdmin)