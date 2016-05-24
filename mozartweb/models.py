# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField("Nom de la ville", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ville"
        verbose_name_plural = "Ville"

@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField("Nom du pays", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pays"
        verbose_name_plural = "Pays"

@python_2_unicode_compatible
class Place(models.Model):
    venue = models.CharField("Lieu", max_length=200)
    city = models.ForeignKey('City')
    country = models.ForeignKey('Country')

    def __str__(self):
        return "%s, %s, %s" % (self.venue, self.city, self.country)

    class Meta:
        verbose_name = "Lieu"
        verbose_name_plural = "Lieu"

@python_2_unicode_compatible
class Type(models.Model):
    type = models.CharField("Nature de l'évènement", max_length=200)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Nature de l'évènement"
        verbose_name_plural = "Nature de l'évènement"

@python_2_unicode_compatible
class Performer(models.Model):
    name = models.CharField("Nom de l'interprète", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Interprète"
        verbose_name_plural = "Interprète"

@python_2_unicode_compatible
class Speech(models.Model):
    title = models.CharField("Titre de la conférence", max_length=200, default="Conférence sans titre")
    speaker = models.ManyToManyField('Speaker', verbose_name='Nome du/de la conférencier/ère', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Conférence"
        verbose_name_plural = "Conférences"

@python_2_unicode_compatible
class Speaker(models.Model):
    name = models.CharField("Nome du/de la conférencier/ère", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Conférencier/ère"
        verbose_name_plural = "Conférencier/ère"

@python_2_unicode_compatible
class Piece(models.Model):
    name = models.CharField("Titre de l'œuvre interpretée", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Œuvre"
        verbose_name_plural = "Œuvre"

@python_2_unicode_compatible
class Event(models.Model):
    """The main class for all 'Mozart' events."""
    title = models.CharField("Titre ou description de l'évènement", max_length=200)
    reference = models.CharField("Référence", max_length=200, null=True, blank=True)
    place = models.ForeignKey('Place', verbose_name='Lieu', null=True, blank=True)
    poster = models.ImageField(upload_to = 'posters', null=True, blank=True, verbose_name='Affiche')
    type = models.ForeignKey('Type', verbose_name="Nature de l'évènement", null=True, blank=True)
    performer = models.ManyToManyField('Performer', verbose_name="Interprètes", blank=True)
    speech = models.ManyToManyField('Speech', verbose_name="Conférence", blank=True)
    piece = models.ManyToManyField('Piece', verbose_name="Œuvres interpretées", blank=True)
    date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Évenement"
        verbose_name_plural = "Évenement"

    def __str__(self):
        return self.title
