# -*- coding: utf-8 -*-

import django_filters
from django.db.models import Q
from models import *
from watson import search as watson
from django.forms import DateInput
from haystack.query import SearchQuerySet

class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(method='custom_title_filter')
    performer = django_filters.CharFilter(label='Interprète ou ensemble/orchestre', method='custom_performer_filter')
    performer__ptype__description = django_filters.ModelChoiceFilter(label='Type interprète', queryset=PerformerType.objects.all())
    piece__name = django_filters.CharFilter(label='Œuvre (titre)', method='custom_piece_filter')
    piece__kochel = django_filters.CharFilter(label='Köchel', method='custom_kochel_filter')
    reference__article_title = django_filters.CharFilter(label="Titre de l'article", method='custom_article_filter')
    reference__journal__title = django_filters.ModelChoiceFilter(label="Journal", queryset=Journal.objects.all())
    reference__author = django_filters.ModelChoiceFilter(label="Auteur de l'article", queryset=Author.objects.all())
    places__city = django_filters.ModelChoiceFilter(label="Ville", queryset=City.objects.all())
    places__country = django_filters.ModelChoiceFilter(label="Pays", queryset=Country.objects.all())
    places__venue = django_filters.CharFilter(label="Lieu", method='custom_venue_filter')
    speech__title = django_filters.CharFilter(label="Titre de la conférence", method='custom_speech_filter')
    speech__speaker = django_filters.CharFilter(label="Conférencier-ère", method='custom_speaker_filter')
    start_date = django_filters.DateFromToRangeFilter(label="Date de l'événement (début - fin jj/mm/aaaa)")
    year_insertion = django_filters.NumberFilter(label="Année d'insertion", name='created_on', lookup_expr='year')
    created_on = django_filters.DateFromToRangeFilter(label="Date d'insertion (début - fin jj/mm/aaaa)")
    comment__content = django_filters.CharFilter(label="Commentaires", method='custom_comments_filter')
    info__content = django_filters.CharFilter(label="Informations complémentaires", method='custom_info_filter')
    created_by__username = django_filters.ModelChoiceFilter(label="Utilisateur", queryset=User.objects.all())
    all_fields = django_filters.CharFilter(label="Chercher dans tous les champs", method='custom_all_filter')

# With the new version of django-filter we can remove the duplication of
# broadcasting model, since it's now possible to look for many models in a
# query

    wordDict = {'ss':'ß', 'oe':'ö', 'ue':'ü', 'ae':'ä'}
    iwordDict = {'ß':'ss', 'ö':'oe', 'ü':'ue', 'ä':'ae'}
    def multipleReplace(self, text, dict_map):
        for key in dict_map:
            text = text.replace(key, dict_map[key])
        return text

    def multipleSearch(self, value, model):
        """
        Do the german/french characters conversion and then perfom the haystack search.
        It returns a list of obj ids to be used by the filter.
        "value" = the search string
        "model" = where to search
        """
        value_converted = self.multipleReplace(value, self.wordDict)
        value_iconverted = self.multipleReplace(value, self.iwordDict)
        result_hs = SearchQuerySet().filter(content=value).models(model) |\
                    SearchQuerySet().filter(content=value_converted).models(model)  |\
                    SearchQuerySet().filter(content=value_iconverted).models(model)
        results = [int(r.pk) for r in result_hs]
        return results

    def custom_title_filter(self, queryset, name, value):
        results = self.multipleSearch(value, Event)
        # quick hack to 'convert' haystack backend querty to a Q query supported by django_filters
        query = (Q(pk__in=results))
        return queryset.filter(query)

    def custom_piece_filter(self, queryset, name, value):
        results = self.multipleSearch(value, Piece)
        query = (Q(piece__in=results))
        return queryset.filter(query)

    def custom_kochel_filter(self, queryset, name, value):
        query = (Q(piece__kochel__iexact=value ))
        return queryset.filter(query)

    def custom_performer_filter(self, queryset, name, value):
        results = self.multipleSearch(value, Performer)
        query = (Q(performer__in=results))
        return queryset.filter(query)

    def custom_speech_filter(self, queryset, name, value):
        results = self.multipleSearch(value, Speech)
        query = (Q(speech__in=results))
        return queryset.filter(query)

    def custom_speaker_filter(self, queryset, name, value):
        results = self.multipleSearch(value, Speaker)
        query = (Q(speech__speaker__in=results))
        return queryset.filter(query)

    def custom_article_filter(self, queryset, name, value):
        results = self.multipleSearch(value, Reference)
        query = (Q(reference__in=results))
        return queryset.filter(query)

    def custom_journal_filter(self, queryset, name, value):
        results = self.multipleSearch(value, Journal)
        query = (Q(reference__journal__in=results))
        return queryset.filter(query)

    def custom_venue_filter(self, queryset, name, value):
        results = self.multipleSearch(value, Place)
        query = (Q(places__in=results))
        return queryset.filter(query)

    def custom_comments_filter(self, queryset, name, value):
        results = self.multipleSearch(value, Comment)
        query = (Q(comment__in=results))
        return queryset.filter(query)

    def custom_info_filter(self, queryset, name, value):
        results = self.multipleSearch(value, AdditionalInfo)
        query = (Q(info__in=results))
        return queryset.filter(query)

    def custom_all_filter(self, queryset, name, value):
        results_event = self.multipleSearch(value, Event)
        results_piece = self.multipleSearch(value, Piece)
        results_venue = self.multipleSearch(value, Place)
        results_article = self.multipleSearch(value, Reference)
        results_journal = self.multipleSearch(value, Journal)
        results_comment = self.multipleSearch(value, Comment)
        results_performer = self.multipleSearch(value, Performer)
        results_speech = self.multipleSearch(value, Speech)
        results_speaker = self.multipleSearch(value, Speaker)
        results_info = self.multipleSearch(value, AdditionalInfo)
        query = (Q(pk__in=results_event) |\
                 Q(piece__in=results_piece) |\
                 Q(places__in=results_venue) |\
                 Q(comment__in=results_comment) |\
                 Q(performer__in=results_performer) |\
                 Q(speech__in=results_speech) |\
                 Q(speech__speaker__in=results_speaker) |\
                 Q(info__in=results_info) |\
                 Q(reference__in=results_article) |\
                 Q(reference__journal__in=results_journal) |\
                 Q(piece__kochel__iexact=value ))

        return queryset.filter(query)


    class Meta:
        model = Event
        fields = [
            'title',
            'type',
            'start_date',
            'piece__name',
            'piece__kochel',
            'performer',
            'performer__ptype__description',
            'speech__title',
            'speech__speaker',
            'reference__article_title',
            'reference__journal__title',
            'reference__author',
            'places__venue',
            'places__city',
            'places__country',
            'comment__content',
            'info__content',
            'created_by__username',
            'year_insertion',
            'created_on',
            'all_fields',
        ]
