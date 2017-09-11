# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-11 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozartweb', '0030_auto_20170903_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='places',
            field=models.ManyToManyField(related_name='places', to='mozartweb.Place', verbose_name='Lieu'),
        ),
    ]
