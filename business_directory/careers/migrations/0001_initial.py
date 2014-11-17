# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
        ('profiles', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('location', models.CharField(max_length=100, verbose_name='Location', blank=True)),
                ('budget_from', models.PositiveIntegerField(null=True, verbose_name='Budget from')),
                ('budget_to', models.PositiveIntegerField(null=True, verbose_name='Budget to')),
                ('status', models.IntegerField(default=0, choices=[(0, 'Archived'), (1, 'Closed'), (2, 'Open')])),
                ('category', models.ForeignKey(to='careers.Category')),
                ('company', models.ForeignKey(to='profiles.CompanyProfile')),
            ],
            options={
                'ordering': ('-created_on',),
                'verbose_name': 'Job Post',
                'verbose_name_plural': 'Job Posts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobPostPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('jobpost', models.ForeignKey(related_name='plugins', to='careers.JobPost')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
