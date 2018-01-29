# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gel.fields
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SilicaPacket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('additional_info', models.CharField(max_length=500, null=True, blank=True)),
                ('found_in', models.CharField(max_length=255, null=True, blank=True)),
                ('manufacturer', tagging.fields.TagField(max_length=255, blank=True)),
                ('text', models.CharField(max_length=255, null=True, blank=True)),
                ('text_languages', tagging.fields.TagField(max_length=255, blank=True)),
                ('print_colors', tagging.fields.TagField(max_length=255, blank=True)),
                ('width', models.IntegerField(null=True, blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
                ('thickness', models.IntegerField(null=True, blank=True)),
                ('weight', models.IntegerField(null=True, blank=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('image', gel.fields.ThumbnailImageField(max_length=140, null=True, upload_to=b'images', blank=True)),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
    ]
