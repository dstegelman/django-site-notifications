from django.db.models import Manager
from django.db.models.query import QuerySet
from datetime import datetime

class NotificationQuerySet(QuerySet):
    def active(self):
        return self.filter(enabled=True)

    def active_notifications(self):
        return self.filter(start_date__lte=datetime.now(), end_date__gte=datetime.now())

class NotificationManager(Manager):
    def get_query_set(self):
        return NotificationQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_query_set().active()

    def active_notifications(self):
        return self.get_query_set().active().active_notifications()