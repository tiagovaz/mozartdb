# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-13 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozartweb', '0002_auto_20170124_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='Commentaire'),
        ),
    ]
