# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-10 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozartweb', '0014_event_bc_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Pr\xe9nom')),
                ('last_name', models.CharField(max_length=200, verbose_name='Nom')),
            ],
            options={
                'ordering': ('last_name',),
                'verbose_name': 'Auteur',
                'verbose_name_plural': 'Auteurs',
            },
        ),
        migrations.AddField(
            model_name='reference',
            name='author',
            field=models.ManyToManyField(blank=True, null=True, to='mozartweb.Author', verbose_name='Auteur(s)'),
        ),
    ]
