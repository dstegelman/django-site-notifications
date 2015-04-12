from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from site_notifications.managers import NotificationManager


STATUS_CHOICES = (
    (40, 'error'),
    (30, 'warning'),
    (25, 'success'),
    (20, 'info')
)


@python_2_unicode_compatible
class Notification(models.Model):
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    enabled = models.BooleanField(default=False)
    message = models.TextField(null=True, blank=False)

    status = models.IntegerField(max_length=20, choices=STATUS_CHOICES, default=20)

    objects = NotificationManager()

    def __str__(self):
        return self.message
