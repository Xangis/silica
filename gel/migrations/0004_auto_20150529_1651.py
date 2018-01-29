# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gel', '0003_auto_20150413_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('slug', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='silicapacket',
            name='manufacturer_id',
            field=models.ForeignKey(blank=True, to='gel.Manufacturer', null=True),
            preserve_default=True,
        ),
    ]
