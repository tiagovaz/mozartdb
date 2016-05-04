# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ville"
        verbose_name_plural = "Ville"

class Country(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pays"
        verbose_name_plural = "Pays"

class Place(models.Model):
    venue = models.CharField(max_length=200)
    city = models.ForeignKey('City')
    country = models.ForeignKey('Country')

    def __str__(self):
        return "%s %s, %s" % (self.venue, self.city, self.country)

    class Meta:
        verbose_name = "Lieu"
        verbose_name_plural = "Lieu"

class Type(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Nature de l'évènement"
        verbose_name_plural = "Nature de l'évènement"

class Performer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Interprète"
        verbose_name_plural = "Interprète"

class Speaker(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Conférencier"
        verbose_name_plural = "Conférencier"

class Piece(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Œuvre"
        verbose_name_plural = "Œuvre"

class Event(models.Model):
    """The main class for all 'Mozart' events."""
    title = models.CharField(max_length=200, null=True, blank=True)
    reference = models.CharField(max_length=200, null=True, blank=True)
    place = models.ForeignKey('Place')
    type = models.ForeignKey('Type')
    performer = models.ManyToManyField('Performer')
    speaker = models.ManyToManyField('Speaker')
    piece = models.ManyToManyField('Piece')
    date = models.DateField()

    class Meta:
        verbose_name = "Évenement"
        verbose_name_plural = "Évenement"

    def __str__(self):
        return self.title
