# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-03 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozartweb', '0029_auto_20170903_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Date d'insertion"),
        ),
    ]
