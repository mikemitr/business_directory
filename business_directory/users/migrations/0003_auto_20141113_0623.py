# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20141112_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyuser',
            name='profile',
        ),
        migrations.DeleteModel(
            name='CompanyUser',
        ),
        migrations.RemoveField(
            model_name='employeeuser',
            name='profile',
        ),
        migrations.DeleteModel(
            name='EmployeeUser',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['email']},
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=255, verbose_name='email address', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.  Unselect this instead of deleting accounts.', verbose_name='active'),
            preserve_default=True,
        ),
    ]
