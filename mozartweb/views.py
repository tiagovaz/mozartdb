from django.shortcuts import render
from dal import autocomplete
from django.views import generic
from django.views.generic import View

from models import *
from mozartweb.filters import EventFilter
from mozartweb.forms import Search

class EventList(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'events'
    model = Event

    def dispatch(self, *args, **kwargs):
        return super(EventList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return EventFilter(self.request.GET, queryset=Event.objects.all())

    def get_context_data(self, **kwargs):
        context = super(EventList, self).get_context_data(**kwargs)

        all_events = EventFilter(self.request.GET, queryset=Event.objects.all())
        context['view'] = "events"
        context['form'] = all_events.form

        return context

class EventDetail(generic.DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'detail.html'

    #TODO: check if we use the same template for anons
    def dispatch(self, *args, **kwargs):
        get_object_or_404(
            Reference,
            id=self.kwargs['pk']
        )
        if self.request.user.is_authenticated():
            self.template_name = 'detail.html'

        return super(EventDetail, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)

        context['form_comment'] = CommentForm()
        context['form_request'] = RequestForm()

        return context

class SearchForm(View):
    def get(self, request):
        search_form = Search()
        return render(request, 'search.html', {'form': search_form})

    def post(self, request):
        pass


class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Country.objects.none()

        qs = Country.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return City.objects.none()

        qs = City.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class PerformerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Performer.objects.none()

        qs = Performer.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class PieceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Piece.objects.none()

        qs = Piece.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class SpeakerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Speaker.objects.none()

        qs = Speaker.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class SpeechAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Speech.objects.none()

        qs = Speech.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class PlaceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Place.objects.none()

        qs = Place.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
