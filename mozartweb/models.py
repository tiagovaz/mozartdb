# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
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
    type = models.CharField("Nature de l'événement", max_length=200)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Nature de l'événement"
        verbose_name_plural = "Nature de l'événement"

@python_2_unicode_compatible
class Reference(models.Model):
    article_title = models.CharField("Titre de l'article", max_length=150, blank=True)
    journal_title = models.CharField("Titre du journal", max_length=150, blank=True)
    page = models.CharField("Page(s)", max_length=150, blank=True)
    date = models.DateField(null=True, verbose_name="Date", blank=True)
    article_file = models.FileField(upload_to='articles', null=True, blank=True, verbose_name='Article en PDF')

    def __str__(self):
        return "« %s », %s, p. %s, %s" % (self.article_title, self.journal_title, self.page, self.date)

    class Meta:
        verbose_name = "Référence"
        verbose_name_plural = "Références"

@python_2_unicode_compatible
class PerformerType(models.Model):
    description = models.CharField("Nature de l'interprète", max_length=200)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Nature de l'interprète"
        verbose_name_plural = "Natures de l'interprète"

@python_2_unicode_compatible
class Performer(models.Model):
    first_name = models.CharField("Prénom (si est une personne)", max_length=200, null=True, blank=True)
    last_name = models.CharField("Nom", max_length=200)
    type = models.ForeignKey('PerformerType', verbose_name='Nature')

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)

    class Meta:
        verbose_name = "Interprète"
        verbose_name_plural = "Interprètes"

@python_2_unicode_compatible
class Speech(models.Model):
    title = models.CharField("Titre de la conférence", max_length=200, default="Conférence sans titre")
    speaker = models.ManyToManyField('Speaker', verbose_name='Nome du/de la conférencier/ère', blank=True)

    def __str__(self):
        #FIXME: return all speakers from this speech
        return self.title + " par " + ", ".join((s.first_name + " " + s.last_name) for s in self.speaker.all())

    class Meta:
        verbose_name = "Conférence"
        verbose_name_plural = "Conférences"

@python_2_unicode_compatible
class RadioStation(models.Model):
    name = models.CharField("Station radio", max_length=200, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Station radio"
        verbose_name_plural = "Station radio"

@python_2_unicode_compatible
class Speaker(models.Model):
    first_name = models.CharField("Prénom", max_length=200)
    last_name = models.CharField("Nom", max_length=200)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)

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
    title = models.CharField("Titre ou description de l'évènement", max_length=201)
    reference = models.ManyToManyField("Reference", blank=True, verbose_name="Référence")
    place = models.ForeignKey('Place', verbose_name='Lieu', null=True, blank=True)
    radio_station = models.ForeignKey('RadioStation', verbose_name='Station radio', null=True, blank=True)
    poster = models.ImageField(upload_to = 'posters', null=True, blank=True, verbose_name='Affiche')
    type = models.ForeignKey('Type', verbose_name="Nature de l'évènement", null=True, blank=True)
    performer = models.ManyToManyField('Performer', verbose_name="Interprètes", blank=True)
    speech = models.ManyToManyField('Speech', verbose_name="Conférence", blank=True)
    piece = models.ManyToManyField('Piece', verbose_name="Œuvres interpretées", blank=True)
    start_date = models.DateField(null=True, verbose_name="Date début de l'événement", blank=True)
    start_time = models.TimeField(null=True, verbose_name="Heure début de l'événement", blank=True)
    end_date = models.DateField(null=True, verbose_name="Date fin de l'événement", blank=True)
    end_time = models.TimeField(null=True, verbose_name="Heure fin de l'événement", blank=True)
    month_is_estimated = models.BooleanField(default=False, verbose_name="Ignorer le mois")
    day_is_estimated = models.BooleanField(default=False, verbose_name="Ignorer le jour")
    relates_to_radio = models.ManyToManyField('Event', verbose_name="Diffusion radio", blank=True)

    created_by = models.ForeignKey(User, related_name='created_by', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    edited_by  = models.ForeignKey(User, related_name='edited_by', null=True, blank=True)
    edited_on  = models.DateTimeField(auto_now = True, null=True, blank=True)

    def comments(self):
    	c = Comment.objects.filter(event=self)

    def diffused_events(self):
        de = Event.objects.filter(relates_to_radio=self)
        return de

    class Meta:
        verbose_name = "Événement"
        verbose_name_plural = "Événement"

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Comment(models.Model):

    content = models.TextField(
        verbose_name="Commentaire"
    )

    created_date = models.DateTimeField(
        verbose_name="Date du commentaire",
        auto_now_add=True
    )

    user = models.ForeignKey(
        User,
        verbose_name="Auteur",
        related_name="comment",
    )

    event = models.ForeignKey(
        'Event',
        verbose_name="Événement",
        related_name="comment"
    )

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return self.content
