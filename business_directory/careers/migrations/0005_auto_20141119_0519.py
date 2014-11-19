# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0004_auto_20141118_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Approved by admin'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jobpostapplied',
            name='resume',
            field=models.FileField(upload_to=b'', storage=django.core.files.storage.FileSystemStorage(location=b'/home/user/python_dev/business_directory/business_directory/media/resumes'), verbose_name='Upload resume'),
            preserve_default=True,
        ),
    ]
