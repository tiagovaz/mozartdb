# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-20 18:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mozartweb', '0017_broadcasting_pdf_checked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='broadcasting',
        ),
    ]