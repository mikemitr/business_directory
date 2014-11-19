# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0003_jobpostapplied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpostapplied',
            name='applicant',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
