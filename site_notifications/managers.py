from datetime import datetime


from django.db.models import Manager
from django.db.models.query import QuerySet


class NotificationQuerySet(QuerySet):

    def active_notifications(self):
        return self.filter(start_date__lte=datetime.now(), end_date__gte=datetime.now(), enabled=True)


class NotificationManager(Manager):
    def get_queryset(self):  # Removed in django1.8
        return NotificationQuerySet(self.model, using=self._db)

    def active_notifications(self):
        return self.get_queryset().active_notifications()
