# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-27 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozartweb', '0006_auto_20170227_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name="Titre de l'\u0153uvre interpret\xe9e"),
        ),
        migrations.AlterField(
            model_name='speech',
            name='speaker',
            field=models.ManyToManyField(blank=True, to='mozartweb.Speaker', verbose_name='Nom du/de la conf\xe9rencier/\xe8re'),
        ),
    ]