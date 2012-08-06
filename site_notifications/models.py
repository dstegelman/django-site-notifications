from django.db import models

class Notification(models.Model):
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    enabled = models.BooleanField()
    message = models.TextField(null=True, blank=False)

    def __unicode__(self):
        return self.message