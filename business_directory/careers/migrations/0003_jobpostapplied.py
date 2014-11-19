# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('django_messages', '__first__'),
        ('careers', '0002_jobpost_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPostApplied',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Applied')),
                ('resume', models.FileField(upload_to=b'', storage=django.core.files.storage.FileSystemStorage(location=b'/media/resumes'), verbose_name='Upload resume')),
                ('applicant', models.ForeignKey(to='profiles.EmployeeProfile')),
                ('jobpost', models.ForeignKey(to='careers.JobPost')),
                ('message', models.ForeignKey(to='django_messages.Message')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
