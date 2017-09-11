# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-11 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozartweb', '0032_auto_20170911_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broadcasting',
            name='place',
        ),
        migrations.AddField(
            model_name='broadcasting',
            name='places',
            field=models.ManyToManyField(related_name='bc_places', to='mozartweb.Place', verbose_name='Lieu'),
        ),
    ]
