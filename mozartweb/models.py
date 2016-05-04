from __future__ import unicode_literals

from django.db import models

class City(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Place(models.Model):
    venue = models.CharField(max_length=200)
    city = models.ForeignKey('City')
    country = models.ForeignKey('Country')

    def __str__(self):
        return "%s %s, %s" % (self.venue, self.city, self.country)

class Type(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

class Performer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Speaker(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Piece(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

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
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title
