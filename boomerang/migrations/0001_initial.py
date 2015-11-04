# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RepeatMSG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=140)),
                ('creation_date', models.DateTimeField(null=True, verbose_name=b'date added')),
                ('delivery_interval', models.IntegerField(verbose_name=b'delivery interval in minutes')),
                ('origin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SimpleMSG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=140)),
                ('creation_date', models.DateTimeField(null=True, verbose_name=b'date added')),
                ('delivery_date', models.DateTimeField(verbose_name=b'date to deliver')),
                ('origin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='simplemsg',
            name='author',
            field=models.ForeignKey(related_name='simple_author', to='boomerang.User'),
        ),
        migrations.AddField(
            model_name='simplemsg',
            name='recipient',
            field=models.ForeignKey(related_name='simple_recipient', to='boomerang.User'),
        ),
        migrations.AddField(
            model_name='repeatmsg',
            name='author',
            field=models.ForeignKey(related_name='repeat_author', to='boomerang.User'),
        ),
        migrations.AddField(
            model_name='repeatmsg',
            name='recipient',
            field=models.ForeignKey(related_name='repeat_recipient', to='boomerang.User'),
        ),
    ]
