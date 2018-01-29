# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
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
        migrations.CreateModel(
            name='Language',
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
            name='print_color',
            field=models.ManyToManyField(to='gel.Color', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='silicapacket',
            name='text_language',
            field=models.ManyToManyField(to='gel.Language', blank=True),
            preserve_default=True,
        ),
    ]
