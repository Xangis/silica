# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gel.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gel', '0006_manufacturer_brands'),
    ]

    operations = [
        migrations.AddField(
            model_name='silicapacket',
            name='rear_image',
            field=gel.fields.ThumbnailImageField(max_length=140, null=True, upload_to=b'images', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='silicapacket',
            name='height',
            field=models.IntegerField(help_text=b'in mm', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='silicapacket',
            name='thickness',
            field=models.IntegerField(help_text=b'in mm', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='silicapacket',
            name='weight',
            field=models.IntegerField(help_text=b'in grams', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='silicapacket',
            name='width',
            field=models.IntegerField(help_text=b'in mm', null=True, blank=True),
            preserve_default=True,
        ),
    ]
