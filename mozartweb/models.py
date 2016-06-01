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
class Reference(models.Model):
    article_title = models.CharField("Titre de l'article", max_length=150, blank=True)
    journal_title = models.CharField("Titre du journal", max_length=150, blank=True)
    page = models.CharField("Page(s)", max_length=150, blank=True)
    date = models.DateField(null=True, verbose_name="Date", blank=True)
    article_file = models.FileField(upload_to='articles', null=True, blank=True, verbose_name='Article en PDF')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = "Réference"
        verbose_name_plural = "Réferences"


@python_2_unicode_compatible
class Performer(models.Model):
    name = models.CharField("Nom de l'interprète", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Interprète"
        verbose_name_plural = "Interprètes"

@python_2_unicode_compatible
class Speech(models.Model):
    title = models.CharField("Titre de la conférence", max_length=200, default="Conférence sans titre")
    speaker = models.ManyToManyField('Speaker', verbose_name='Nome du/de la conférencier/ère', blank=True)

    def __str__(self):
        #FIXME: return all speakers from this speech
        return self.title + " par " + "".join(s.name for s in self.speaker.all())

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
        verbose_name_plural = "Conférenciers/ères"

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
    reference = models.ForeignKey("Reference", blank=True, null=True)
    place = models.ForeignKey('Place', verbose_name='Lieu', null=True, blank=True)
    poster = models.ImageField(upload_to = 'posters', null=True, blank=True, verbose_name='Affiche')
    type = models.ForeignKey('Type', verbose_name="Nature de l'évènement", null=True, blank=True)
    performer = models.ManyToManyField('Performer', verbose_name="Interprètes", blank=True)
    speech = models.ManyToManyField('Speech', verbose_name="Conférence", blank=True)
    piece = models.ManyToManyField('Piece', verbose_name="Œuvres interpretées", blank=True)
    start_date = models.DateField(null=True, verbose_name="Début de l'évenement", blank=True)
    end_date = models.DateField(null=True, verbose_name="Fin de l'évenement", blank=True)

    class Meta:
        verbose_name = "Évenement"
        verbose_name_plural = "Évenement"

    def __str__(self):
        return self.title
