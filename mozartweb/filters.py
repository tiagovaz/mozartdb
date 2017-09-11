# -*- coding: utf-8 -*-

import django_filters

from models import *

class EventFilter(django_filters.FilterSet):
#    title = django_filters.MethodFilter(label="Titre de l'événement", action='filter_title')
    title = django_filters.CharFilter(label="Titre de l'événement", lookup_expr='icontains')
    performer__last_name = django_filters.CharFilter(label='Interprète / ensemble', lookup_expr='icontains')
    performer__type = django_filters.ModelChoiceFilter(label='Type interprète', queryset=PerformerType.objects.all())
    piece__name = django_filters.CharFilter(label='Œuvre', lookup_expr='icontains')
    reference__article_title = django_filters.CharFilter(label="Titre de l'article", lookup_expr='icontains')
    reference__journal_title = django_filters.CharFilter(label="Titre du journal", lookup_expr='icontains')
    places__city = django_filters.ModelChoiceFilter(label="Ville", queryset=City.objects.all())
    places__country = django_filters.ModelChoiceFilter(label="Pays", queryset=Country.objects.all())
    places__venue = django_filters.CharFilter(label="Lieu", lookup_expr='icontains')
    speech__title = django_filters.CharFilter(label="Titre de la conférence", lookup_expr='icontains')
    speech__speaker__last_name = django_filters.CharFilter(label="Conférencier-ère", lookup_expr='icontains')
    #year = django_filters.MethodFilter(label='Année', action='year_range')
    start_date = django_filters.DateFromToRangeFilter(label="Date de l'événement (début - fin jj/mm/aaaa)")
    #year = django_filters.NumberFilter(label='Année', name='start_date', lookup_expr='year')
    #month = django_filters.NumberFilter(label='Mois', name='start_date', lookup_expr='month')
    year_insertion = django_filters.NumberFilter(label="Année d'insertion", name='created_on', lookup_expr='year')
    created_on = django_filters.DateFromToRangeFilter(label="Date d'insertion (début - fin jj/mm/aaaa)")
    comment__content = django_filters.CharFilter(label="Commentaires", lookup_expr='icontains')
    created_by__username = django_filters.ModelChoiceFilter(label="Utilisateur", queryset=User.objects.all())

 #   def year_range(self, queryset, value):
 #       return queryset.filter()

    class Meta:
        model = Event
        fields = [
            'title',
            'type',
            'piece__name',
            'performer__last_name',
            'performer__type',
            'speech__title',
            'speech__speaker__last_name',
            'reference__article_title',
            'reference__journal_title',
            'places__venue',
            'places__city',
            'places__country',
            'start_date',
            'pdf_checked',
            'comment__content',
            'created_by__username',
            'year_insertion',
            'created_on',
        ]

    def filter_title(self, queryset, value):
        return queryset.filter(relates_to_broadcasting__title__icontains=value) | queryset.filter(title__icontains=value)
