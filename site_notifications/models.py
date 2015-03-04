from django.db import models

from site_notifications.managers import NotificationManager
from site_notifications.choices import STATUS_CHOICES

class Notification(models.Model):
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    enabled = models.BooleanField(default=False)
    message = models.TextField(null=True, blank=False)

    status = models.IntegerField(max_length=20, choices=STATUS_CHOICES, default=20)

    objects = NotificationManager()

    def __unicode__(self):
        return self.message
