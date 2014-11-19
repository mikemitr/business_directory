# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='user',
            field=models.OneToOneField(related_name='company', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='user',
            field=models.OneToOneField(related_name='employee', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
