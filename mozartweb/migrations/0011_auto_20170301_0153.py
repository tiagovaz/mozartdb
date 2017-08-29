# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-01 01:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mozartweb', '0010_auto_20170227_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcasting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=201, verbose_name='Titre ou description de la radiodiffusion')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Date d\xe9but de la radiodiffusion')),
                ('start_time', models.TimeField(blank=True, null=True, verbose_name='Heure d\xe9but de la radiodiffusion')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Date fin de la radiodiffusion')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='Heure fin de la radiodiffusion')),
                ('month_is_estimated', models.BooleanField(default=False, verbose_name='Ignorer le mois')),
                ('day_is_estimated', models.BooleanField(default=False, verbose_name='Ignorer le jour')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('edited_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rd_created_by', to=settings.AUTH_USER_MODEL)),
                ('edited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rd_edited_by', to=settings.AUTH_USER_MODEL)),
                ('performer', models.ManyToManyField(blank=True, to='mozartweb.Performer', verbose_name='Interpr\xe8tes')),
                ('piece', models.ManyToManyField(blank=True, to='mozartweb.Piece', verbose_name='\u0152uvres interpret\xe9es')),
                ('radio_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mozartweb.RadioStation', verbose_name='Station radio')),
                ('reference', models.ManyToManyField(blank=True, to='mozartweb.Reference', verbose_name='R\xe9f\xe9rence')),
                ('speech', models.ManyToManyField(blank=True, to='mozartweb.Speech', verbose_name='Conf\xe9rence')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Radiodiffusion',
                'verbose_name_plural': 'Radiodiffusion',
            },
        ),
        migrations.CreateModel(
            name='TypeBroadcasting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200, verbose_name='Nature de la diffusion')),
            ],
            options={
                'ordering': ('type',),
                'verbose_name': 'Nature de la diffusion',
                'verbose_name_plural': 'Nature de la diffusion',
            },
        ),
        migrations.AlterField(
            model_name='event',
            name='relates_to_radio',
            field=models.ManyToManyField(blank=True, to='mozartweb.Event', verbose_name='Diffusion radio (ancienne)'),
        ),
        migrations.AddField(
            model_name='broadcasting',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mozartweb.TypeBroadcasting', verbose_name='Nature'),
        ),
        migrations.AddField(
            model_name='comment',
            name='broadcasting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='mozartweb.Broadcasting', verbose_name='Radiodiffusion'),
        ),
        migrations.AddField(
            model_name='event',
            name='relates_to_broadcasting',
            field=models.ManyToManyField(blank=True, to='mozartweb.Broadcasting', verbose_name='Diffusion radio'),
        ),
    ]
