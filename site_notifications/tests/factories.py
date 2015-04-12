import factory

import datetime


from site_notifications.models import Notification


class NotificationFactory(factory.DjangoModelFactory):
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now() + datetime.timedelta(days=2)

    class Meta:
        model = Notification