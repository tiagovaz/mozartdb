# -*- coding: utf-8 -*-

import django_filters

from models import *


class EventFilter(django_filters.FilterSet):
    speech__speaker = django_filters.CharFilter(label="Conférencier-ère", lookup_expr='icontains')
    title = django_filters.CharFilter(label="Titre de l'événement", lookup_expr='icontains')
    performer__last_name = django_filters.CharFilter(label='Interprète / ensemble', lookup_expr='icontains')
    performer__type = django_filters.ModelChoiceFilter(label='Type interprète', queryset=PerformerType.objects.all())
    piece__name = django_filters.CharFilter(label='Œuvre', lookup_expr='icontains')
    reference__article_title = django_filters.CharFilter(label="Titre de l'article", lookup_expr='icontains')
    reference__journal_title = django_filters.CharFilter(label="Titre du journal", lookup_expr='icontains')
    place__city = django_filters.ModelChoiceFilter(label="Ville", queryset=City.objects.all())
    place__country = django_filters.ModelChoiceFilter(label="Pays", queryset=Country.objects.all())
    place__venue = django_filters.CharFilter(label="Lieu", lookup_expr='icontains')
    speech__title = django_filters.CharFilter(label="Titre de la conférence", lookup_expr='icontains')
    #year = django_filters.MethodFilter(label='Année', action='year_range')
    year = django_filters.NumberFilter(label='Année', name='start_date', lookup_expr='year')
    month = django_filters.NumberFilter(label='Mois', name='start_date', lookup_expr='month')
    comment__content = django_filters.CharFilter(label="Commentaires", lookup_expr='icontains')

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
            'speech__speaker',
            'reference__article_title',
            'reference__journal_title',
            'place__venue',
            'place__city',
            'place__country',
            'month',
            'year',
            'comment__content',
        ]
