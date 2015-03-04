from django.db.models import Manager
from django.db.models.query import QuerySet
from datetime import datetime

class NotificationQuerySet(QuerySet):
    def active(self):
        return self.filter(enabled=True)

    def active_notifications(self):
        return self.filter(start_date__lte=datetime.now(), end_date__gte=datetime.now())

class NotificationManager(Manager):
    def get_query_set(self):  # Removed in django1.8
        return NotificationQuerySet(self.model, using=self._db)

    def get_queryset(self):
        return self.get_queryset()

    def active(self):
        return self.get_queryset().active()

    def active_notifications(self):
        return self.get_queryset().active().active_notifications()
