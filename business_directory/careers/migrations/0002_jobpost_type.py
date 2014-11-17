# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='type',
            field=models.CharField(default=b'ft', max_length=2, choices=[(b'pt', 'Part Time'), (b'ft', 'Full Time'), (b'ct', 'Contract')]),
            preserve_default=False,
        ),
    ]
