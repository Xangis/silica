# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gel', '0007_auto_20160508_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='website',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
