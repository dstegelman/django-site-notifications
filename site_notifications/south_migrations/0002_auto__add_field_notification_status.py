# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Notification.status'
        db.add_column('site_notifications_notification', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=20, max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Notification.status'
        db.delete_column('site_notifications_notification', 'status')


    models = {
        'site_notifications.notification': {
            'Meta': {'object_name': 'Notification'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': "20", 'max_length': '20'})
        }
    }

    complete_apps = ['site_notifications']