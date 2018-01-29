# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gel', '0002_auto_20150413_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='silicapacket',
            name='print_colors',
        ),
        migrations.RemoveField(
            model_name='silicapacket',
            name='text_languages',
        ),
    ]
