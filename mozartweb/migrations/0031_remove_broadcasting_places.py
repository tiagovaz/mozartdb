# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-11 15:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mozartweb', '0030_auto_20170911_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broadcasting',
            name='places',
        ),
    ]