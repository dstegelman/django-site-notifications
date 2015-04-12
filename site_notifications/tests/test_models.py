from django.test import TestCase

from site_notifications.tests.factories import NotificationFactory
from site_notifications.models import Notification


class SiteNotificationsModelTest(TestCase):

    def setUp(self):
        self.notification = NotificationFactory.create()

    def test_active(self):
        self.assertTrue(Notification.objects.active_notifications().count())

    def test_inactive(self):
        self.notification.enabled = False
        self.notification.save()

        self.assertFalse(Notification.objects.active_notifications().count())