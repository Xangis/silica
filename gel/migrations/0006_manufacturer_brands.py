# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gel', '0005_remove_silicapacket_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='brands',
            field=models.CharField(max_length=120, null=True, blank=True),
            preserve_default=True,
        ),
    ]
