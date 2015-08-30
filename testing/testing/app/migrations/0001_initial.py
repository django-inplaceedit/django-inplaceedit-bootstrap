# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alert_type', models.CharField(max_length=10, verbose_name='Alert type', choices=[(b'default', 'Default'), (b'primary', 'Primary'), (b'success', 'Success'), (b'info', 'Info'), (b'warning', 'Warning'), (b'danger', 'Danger')])),
                ('msg', models.TextField(verbose_name='Msg')),
            ],
            options={
                'verbose_name': 'Alert',
                'verbose_name_plural': 'Alerts',
            },
        ),
        migrations.CreateModel(
            name='Chunk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=100, verbose_name='key', db_index=True)),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Chunk',
                'verbose_name_plural': 'Chunks',
            },
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('panel_type', models.CharField(max_length=10, verbose_name='Color type', choices=[(b'default', 'Default'), (b'primary', 'Primary'), (b'success', 'Success'), (b'info', 'Info'), (b'warning', 'Warning'), (b'danger', 'Danger')])),
                ('creation_time', models.DateTimeField(verbose_name='Creation time')),
                ('content', models.TextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Panel',
                'verbose_name_plural': 'Panels',
            },
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alt', models.CharField(max_length=200, verbose_name='Alt')),
                ('img', models.ImageField(upload_to=b'thumbnails', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Thumbnail',
                'verbose_name_plural': 'Thumbnails',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=100, verbose_name='key', db_index=True)),
                ('text', models.CharField(max_length=100, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Title',
                'verbose_name_plural': 'Titles',
            },
        ),
    ]
