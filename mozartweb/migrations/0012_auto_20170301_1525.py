# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-01 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mozartweb', '0011_auto_20170301_0153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='performertype',
            options={'ordering': ('description',), 'verbose_name': "Nature de l'interpr\xe8te", 'verbose_name_plural': "Nature de l'interpr\xe8te"},
        ),
        migrations.RemoveField(
            model_name='event',
            name='relates_to_radio',
        ),
    ]