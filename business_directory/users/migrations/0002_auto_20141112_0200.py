# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=100, verbose_name='company name', blank=True)),
            ],
            options={
                'db_table': 'company_user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmployeeUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'employee_user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employeeuser',
            name='profile',
            field=models.ForeignKey(to='users.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='companyuser',
            name='profile',
            field=models.ForeignKey(to='users.UserProfile'),
            preserve_default=True,
        ),
    ]
