# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boomerang', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repeatmsg',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='simplemsg',
            name='origin',
        ),
    ]
