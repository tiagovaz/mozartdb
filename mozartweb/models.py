# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
import locale
import re
from mozartweb import signals
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8") 
import sys
reload(sys)
sys.setdefaultencoding('utf8')

@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField("Nom de la ville", max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ville"
        verbose_name_plural = "Ville"
        ordering = ('name',)

@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField("Nom du pays", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pays"
        verbose_name_plural = "Pays"
        ordering = ('name',)

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
        ordering = ('venue',)
        unique_together = (("city", "country", "venue"),)

@python_2_unicode_compatible
class Type(models.Model):
    type = models.CharField("Nature de l'événement", max_length=200)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Nature de l'événement"
        verbose_name_plural = "Nature de l'événement"
        ordering = ('type',)

@python_2_unicode_compatible
class TypeBroadcasting(models.Model):
    type = models.CharField("Nature de la diffusion", max_length=200)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Nature de la diffusion"
        verbose_name_plural = "Nature de la diffusion"
        ordering = ('type',)

@python_2_unicode_compatible
class Journal(models.Model):
    title = models.CharField("Titre du journal", max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Titre du journal"
        verbose_name_plural = "Titre du journal"
        ordering = ('title',)

@python_2_unicode_compatible
class Reference(models.Model):
    article_title = models.CharField("Titre de l'article", max_length=150, blank=True)
    journal = models.ForeignKey("Journal", verbose_name="Titre du journal", blank=True, null=True)
    author = models.ManyToManyField('Author', verbose_name='Auteur(s)', blank=True, null=True)
    page = models.CharField("Page(s)", max_length=150, blank=True)
    date = models.DateField(null=True, verbose_name="Date", blank=True)
    article_file = models.FileField(upload_to='articles', null=True, blank=True, verbose_name='Article en PDF')

    def __str__(self):
        li = []
        authors = self.author.all()
        for a in authors:
            if a is not None:
                li.append(a.get_fullname())
        author_all = " et ".join(li)
        if self.page:
            page = ", p. %s" % (self.page)
        else:
            page = ""
        if self.date:
            date = ", %s" % (self.date)
        else:
            date = ""
        if author_all:
            author = "%s, " % (author_all)
        else:
            author = ""
        if self.journal:
            journal = ", %s" % (self.journal.title)
        else:
            journal = ""
        article = "« %s »" % (self.article_title)
        return "%s%s%s%s%s" % (author, article, journal, date, page)

    class Meta:
        verbose_name = "Référence"
        verbose_name_plural = "Références"
	ordering = ('article_title',)
        #unique_together = (("article_title", "journal_title", "page", "date", "author"),)

@python_2_unicode_compatible
class PerformerType(models.Model):
    description = models.CharField("Nature de l'interprète", max_length=200)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Nature de l'interprète"
        verbose_name_plural = "Nature de l'interprète"
        ordering = ('description',)

from django.core.exceptions import ObjectDoesNotExist

@python_2_unicode_compatible
class Performer(models.Model):
    first_name = models.CharField("Prénom (si est une personne)", max_length=200, null=True, blank=True)
    last_name = models.CharField("Nom", max_length=200)
    ptype = models.ManyToManyField('PerformerType', related_name='ptype', verbose_name='Nature')

    def get_fullname(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        li = []
        ptypes = self.ptype.all()
        for p in ptypes:
            if p is not None:
                li.append(p.description)
        ptypes_all = ", ".join(li)

        try:
            return "%s, %s [%s]" % (self.last_name, self.first_name, ptypes_all)
        except ObjectDoesNotExist:
            return "%s, %s" % (self.last_name, self.first_name)
      #  return "%s, %s" % (self.last_name, self.first_name)

    class Meta:
        verbose_name = "Interprète"
        verbose_name_plural = "Interprètes"
        ordering = ('last_name',)
#        unique_together = (("first_name", "last_name", "ptype"),) #FIXME: ptype is m2m

@python_2_unicode_compatible
class Speech(models.Model):
    title = models.CharField("Titre de la conférence", max_length=200, default="Conférence sans titre")
    speaker = models.ManyToManyField('Speaker', verbose_name='Nom du/de la conférencier/ère', blank=True)

    def __str__(self):
        #FIXME: return all speakers from this speech
        return self.title + " par " + ", ".join((s.first_name + " " + s.last_name) for s in self.speaker.all())

    class Meta:
        verbose_name = "Conférence"
        verbose_name_plural = "Conférences"
        ordering = ('title',)

@python_2_unicode_compatible
class RadioStation(models.Model):
    name = models.CharField("Station radio", max_length=200, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Station radio"
        verbose_name_plural = "Station radio"
        ordering = ('name',)

@python_2_unicode_compatible
class Speaker(models.Model):
    first_name = models.CharField("Prénom", max_length=200, null=True, blank=True)
    last_name = models.CharField("Nom", max_length=200)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)

    def get_fullname(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Conférencier/ère"
        verbose_name_plural = "Conférenciers/ères"
        ordering = ('last_name',)
#        unique_together = ("first_name", "last_name")

@python_2_unicode_compatible
class Author(models.Model):
    first_name = models.CharField("Prénom", max_length=200, null=True, blank=True)
    last_name = models.CharField("Nom", max_length=200)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)

    def get_fullname(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"
        ordering = ('last_name',)

@python_2_unicode_compatible
class Piece(models.Model):
    name = models.CharField("Titre de l'œuvre interpretée", max_length=200)
    kochel = models.CharField("Köchel", max_length=20, blank=True, null=True)

    def __str__(self):
        o = re.sub(', K. \w+', '', self.name)
        if self.kochel:
            o = o + ", K. " + self.kochel
        return o

    class Meta:
        verbose_name = "Œuvre"
        verbose_name_plural = "Œuvre"
        ordering = ('name',)
        unique_together = ('name', 'kochel')

@python_2_unicode_compatible
class AdditionalInfo(models.Model):
    content = models.TextField("Informations complémentaires", null=True, blank=True)

    created_on = models.DateTimeField(
        verbose_name="Date d'insertion",
        auto_now_add=True
    )

    created_by = models.ForeignKey(
        User,
        verbose_name="Auteur",
        related_name="info",
    )

    event = models.ForeignKey(
        'Event',
        verbose_name="Événement",
        related_name="info", null=True, blank=True
    )

    class Meta:
        verbose_name = "Informations complémentaires"
        verbose_name_plural = "Informations complémentaires"

    def __str__(self):
        ret = self.content + " -- par " + self.created_by.first_name +  " " + self.created_by.last_name + " le " + str(self.created_on)
        return ret

class AdditionalInfoLog(models.Model):
    changed_on = models.DateTimeField(
        verbose_name="Date de modification",
        auto_now_add=True
    )

    changed_by = models.ForeignKey(
        User,
        verbose_name="Auteur",
    )

    info = models.ForeignKey(
        'AdditionalInfo',
        verbose_name="Informations",
        related_name="log"
    )

    class Meta:
        verbose_name = "Informations complémentaires LOG"
        verbose_name_plural = "Informations complémentaires LOG"

    def __str__(self):
        ret = str(self.info.id) + " at " + str(self.changed_on) + " by " + self.changed_by.first_name
        return ret

@python_2_unicode_compatible
class Event(models.Model):
    """The main class for all 'Mozart' events."""
    title = models.CharField("Titre ou description de l'évènement", max_length=201)
    reference = models.ManyToManyField("Reference", blank=True, verbose_name="Référence")
    places = models.ManyToManyField('Place', verbose_name='Lieu', related_name='places', blank=True)
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
    month_is_estimated = models.BooleanField(default=False, verbose_name="Ignorer le mois et le jour")
    day_is_estimated = models.BooleanField(default=False, verbose_name="Ignorer le jour")
    relates_to_broadcasting = models.ManyToManyField('Broadcasting', verbose_name="Diffusion radio", blank=True)

    created_by = models.ForeignKey(User, related_name='created_by', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    edited_by  = models.ForeignKey(User, related_name='edited_by', null=True, blank=True)
    edited_on  = models.DateTimeField(auto_now = True, null=True, blank=True)

    bc_key = models.ForeignKey('Broadcasting', related_name='bc_key', verbose_name='BC KEY (ne pas changer!)', null=True, blank=True)

    def get_info(self):
        info_list = []
        for i in AdditionalInfo.objects.filter(event=self).all():
            info_list.append(i)
        return info_list

    def get_comments(self):
        c_list = []
        for c in Comment.objects.filter(event=self).all():
            c_list.append(c)
        return c_list

    # FIXME: ???
    def comments(self):
    	c = Comment.objects.filter(broadcasting=self)

    def _format_date(self, date):
        if date is not None:
            if self.month_is_estimated:
                return date.strftime("%Y")
            elif self.day_is_estimated:
                return date.strftime("%B %Y")
            else:
                return date.strftime("%d %B %Y")
        else:
            return None

    def _format_date_sortable(self, date):
        if date is not None:
            if self.month_is_estimated:
                return date.strftime("%Y")
            elif self.day_is_estimated:
                return date.strftime("%Y-%m")
            else:
                return date.strftime("%Y-%m-%d")
        else:
            return None

    def get_previous(self):
        event = Event.objects.filter(id__lt=self.id).order_by('-id').first()
        if self == Event.objects.all().order_by('id').first():
            return self
        else:
            return event

    def get_next(self):
        event = Event.objects.filter(id__gt=self.id).order_by('id').first()
        if self == Event.objects.all().order_by('id').last():
            return self
        else:
            return event
    
    def format_start_date(self):
        return self._format_date(self.start_date)

    def format_start_date_sortable(self):
        return self._format_date_sortable(self.start_date)

    def format_end_date(self):
        return self._format_date(self.end_date)

    def format_end_date_sortable(self):
        return self._format_date_sortable(self.end_date)

    class Meta:
        verbose_name = "Événement"
        verbose_name_plural = "Événement"
        ordering = ('title',)

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Broadcasting(models.Model):
    """The class for 'radiodiffusion'"""
    title = models.CharField("Titre ou description de la radiodiffusion", max_length=201)
    reference = models.ManyToManyField("Reference", blank=True, verbose_name="Référence")
    radio_station = models.ForeignKey('RadioStation', verbose_name='Station radio', null=True, blank=True)
    type = models.ForeignKey('TypeBroadcasting', verbose_name="Nature", null=True, blank=True)
    performer = models.ManyToManyField('Performer', verbose_name="Interprètes", blank=True)
    speech = models.ManyToManyField('Speech', verbose_name="Conférence", blank=True)
    piece = models.ManyToManyField('Piece', verbose_name="Œuvres interpretées", blank=True)
    start_date = models.DateField(null=True, verbose_name="Date début de la radiodiffusion", blank=True)
    start_time = models.TimeField(null=True, verbose_name="Heure début de la radiodiffusion", blank=True)
    end_date = models.DateField(null=True, verbose_name="Date fin de la radiodiffusion", blank=True)
    end_time = models.TimeField(null=True, verbose_name="Heure fin de la radiodiffusion", blank=True)
    month_is_estimated = models.BooleanField(default=False, verbose_name="Ignorer le mois")
    day_is_estimated = models.BooleanField(default=False, verbose_name="Ignorer le jour")

    created_by = models.ForeignKey(User, related_name='rd_created_by', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    edited_by  = models.ForeignKey(User, related_name='rd_edited_by', null=True, blank=True)
    edited_on  = models.DateTimeField(auto_now = True, null=True, blank=True)

    def ev_clone(self):
        ev = Event.objects.get(bc_key=self)
        return ev

    def comments(self):
    	c = Comment.objects.filter(event=self)

    def get_related_events(self):
        events_list = Event.objects.filter(relates_to_broadcasting=self)
        return events_list

    class Meta:
        verbose_name = "Radiodiffusion"
        verbose_name_plural = "Radiodiffusion"
        ordering = ('title',)

    def __str__(self):
        return self.title

# duplicate radiodiffusion to an event object
# this workaround is done to allow us keep using a single django_filter search
# for all events
# every change in the event model should be considered here
def save_broadcasting(sender, instance, **kwargs):
    event = Event.objects.filter(bc_key=instance)
    if not event:
        my_event = Event.objects.create(title = instance.title)
        my_event.bc_key = instance
    else:
        my_event = Event.objects.get(bc_key=instance)

    if instance.radio_station:
        radio = RadioStation.objects.get(name=instance.radio_station)
        my_event.radio_station = radio
    else:
        my_event.radio_station = None
 
    if instance.type:
        t = Type.objects.get(type=instance.type)
        my_event.type = t
    else:
        my_event.type = None

    my_event.title = instance.title
    my_event.start_date = instance.start_date
    my_event.start_time = instance.start_time
    my_event.end_date = instance.end_date
    my_event.end_time = instance.end_time
    my_event.month_is_estimated = instance.month_is_estimated
    my_event.day_is_estimated = instance.day_is_estimated
    my_event.created_by = instance.created_by
    my_event.created_on = instance.created_on
    my_event.edited_by  = instance.edited_by
    my_event.edited_on  = instance.edited_on
 
    my_event.save()

post_save.connect(save_broadcasting, sender=Broadcasting)

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
        related_name="comment", null=True, blank=True
    )


    class Meta:
        verbose_name = "Commentaire interne"
        verbose_name_plural = "Commentaires internes"

    def __str__(self):
        ret = self.content + " -- par " + self.user.first_name +  " " + self.user.last_name + " le " + str(self.created_date)
        return ret

# Needs receivers to duplicate manytomany fields
@receiver(m2m_changed, sender = Broadcasting.reference.through)
def m2m(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    my_event = Event.objects.get(bc_key=instance)
    my_event.reference = instance.reference.all()
    my_event.save()

m2m_changed.connect(m2m, sender = Broadcasting.reference.through, dispatch_uid = 'foo', weak = False)

@receiver(m2m_changed, sender = Broadcasting.performer.through)
def m2m(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    my_event = Event.objects.get(bc_key=instance)
    my_event.performer = instance.performer.all()
    my_event.save()

m2m_changed.connect(m2m, sender = Broadcasting.performer.through, dispatch_uid = 'foo', weak = False)

@receiver(m2m_changed, sender = Broadcasting.speech.through)
def m2m(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    my_event = Event.objects.get(bc_key=instance)
    my_event.speech = instance.speech.all()
    my_event.save()

m2m_changed.connect(m2m, sender = Broadcasting.speech.through, dispatch_uid = 'foo', weak = False)

@receiver(m2m_changed, sender = Broadcasting.piece.through)
def m2m(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    my_event = Event.objects.get(bc_key=instance)
    my_event.piece = instance.piece.all()
    my_event.save()

m2m_changed.connect(m2m, sender = Broadcasting.piece.through, dispatch_uid = 'foo', weak = False)

models.signals.post_save.connect(
    signals.add_info_log,
    sender=AdditionalInfo
)

# Redis clear cache signals
models.signals.post_save.connect(
    signals.clear_event_cache,
    sender=Event
)
models.signals.post_save.connect(
    signals.clear_comment_cache,
    sender=Comment
)
models.signals.post_save.connect(
    signals.clear_info_cache,
    sender=AdditionalInfo
)

models.signals.post_delete.connect(
    signals.clear_event_cache,
    sender=Event
)
models.signals.post_delete.connect(
    signals.clear_comment_cache,
    sender=Comment
)
models.signals.post_delete.connect(
    signals.clear_info_cache,
    sender=AdditionalInfo
)

