# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('enabled', models.BooleanField(default=False)),
                ('message', models.TextField(null=True)),
                ('status', models.IntegerField(default=20, max_length=20, choices=[(40, b'error'), (30, b'warning'), (25, b'success'), (20, b'info')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
