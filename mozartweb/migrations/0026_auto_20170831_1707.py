# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-31 17:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mozartweb', '0025_auto_20170831_1659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Commentaire interne', 'verbose_name_plural': 'Commentaires internes'},
        ),
    ]