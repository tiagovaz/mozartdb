from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from dal import autocomplete
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import DeleteView

from models import *
from mozartweb.filters import EventFilter
from mozartweb.forms import Search, CommentForm, EventForm
from django.http import HttpResponse
import csv

class EventList(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'events'
    model = Event

    def dispatch(self, *args, **kwargs):
        return super(EventList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        if not dict(self.request.GET.lists()):
            return EventFilter(self.request.GET, queryset=Event.objects.all().order_by('-id')[:25])
        else:
            return EventFilter(self.request.GET, queryset=Event.objects.all().distinct())

    def get_context_data(self, **kwargs):
        context = super(EventList, self).get_context_data(**kwargs)

        all_events = EventFilter(self.request.GET, queryset=Event.objects.all().distinct())
        context['view'] = "events"
        context['form'] = all_events.form

        return context

class EventDetail(generic.DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'detail.html'

    def dispatch(self, *args, **kwargs):
        get_object_or_404(
            Event,
            id=self.kwargs['pk']
        )
        return super(EventDetail, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context['form_comment'] = CommentForm()
        return context

class BroadcastingDetail(generic.DetailView):
    model = Broadcasting
    context_object_name = 'broadcasting'
    template_name = 'broadcasting_detail.html'

    def dispatch(self, *args, **kwargs):
        get_object_or_404(
            Broadcasting,
            id=self.kwargs['pk']
        )
        return super(BroadcastingDetail, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BroadcastingDetail, self).get_context_data(**kwargs)
        context['form_comment'] = CommentForm()
        return context

class SearchForm(View):
    def get(self, request):
        search_form = Search()
        return render(request, 'search.html', {'form': search_form})

    def post(self, request):
        pass

class EventCreate(generic.CreateView):
    model = Event
    template_name = 'create_event.html'
    form = EventForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.event = Event.objects.get(id=self.kwargs['pk'])
        return super(EventCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'event_detail',
            kwargs={'pk': self.kwargs['pk']}
        )

class CommentCreate(generic.CreateView):
    model = Comment
    template_name = 'create_comment.html'
    fields = [
        'content'
    ]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CommentCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.event = Event.objects.get(id=self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'event_detail',
            kwargs={'pk': self.kwargs['pk']}
        )

class Login(generic.TemplateView):
    template_name = 'login.html'
