# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-01 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mozartweb', '0012_auto_20170301_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='mozartweb.Event', verbose_name='\xc9v\xe9nement'),
        ),
    ]
