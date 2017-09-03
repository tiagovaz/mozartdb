# -*- coding: utf-8 -*-

from django.contrib import admin
from django.forms import TextInput, Textarea
from easy_select2 import select2_modelform, select2_modelform_meta
#from mozartweb.forms import RadioDiffusionForm
from mozartweb.models import City, AdditionalInfo, Country, Type, TypeBroadcasting, Speech, Reference, Place, Performer, Piece, Speaker, RadioStation, PerformerType, Comment, Event, Broadcasting, Author, AdditionalInfo, AdditionalInfoLog
from django import forms
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ManyToManyWidget
from import_export import fields

class EventResource(resources.ModelResource):
    def dehydrate_performer(self, event):
        performers = []
        for p in event.performer.all():
            performers.append(p)
        return str(performers).decode('utf-8')

    def dehydrate_reference(self, event):
        references = []
        for p in event.reference.all():
            references.append(p)
        return str(references).decode('utf-8')

    def dehydrate_speech(self, event):
        speechs = []
        for p in event.speech.all():
            speechs.append(p)
        return str(speechs).decode('utf-8')

    def dehydrate_piece(self, event):
        pieces = []
        for p in event.piece.all():
            pieces.append(p)
        return str(pieces).decode('utf-8')

    def dehydrate_relates_to_broadcasting(self, event):
        bs = []
        for p in event.relates_to_broadcasting.all():
            bs.append(p)
        return str(bs).decode('utf-8')

    class Meta:
        performer = fields.Field(widget=ManyToManyWidget(Performer))
        fields = ('id',
#                  'title',
                  'reference', #
#                  'place__venue',
#                  'place__city__name', 
#                  'place__country__name',
#                  'radio_station__name', 
#                  'type__type', 
                  'performer',  #
                  'speech',  #
                  'piece', #
#                  'start_date', 
#                  'start_time', 
#                  'end_date', 
#                  'end_time', 
#                  'month_is_estimated', 
#                  'day_is_estimated', 
#                  'pdf_checked', 
                  'relates_to_broadcasting', #
#                  'created_by', 
#                  'created_on', 
#                  'edited_by', 
#                  'comments', #
#                  'info', #
                 )
        model = Event

#EventForm = select2_modelform(Event, attrs={'width': '640px'})
# Another way to set easy_select2:
class EventForm(forms.ModelForm):
    Meta = select2_modelform_meta(Event, attrs={'width': '530px'})

BroadcastingForm = select2_modelform(Broadcasting, attrs={'width': '530px'})
PlaceForm = select2_modelform(Place)
RadioStationForm = select2_modelform(RadioStation)
SpeechForm = select2_modelform(Speech)
PerformerForm = select2_modelform(Performer)
ReferenceForm = select2_modelform(Reference)

class PlaceAdmin(admin.ModelAdmin):
    form = PlaceForm

class RadioStationAdmin(admin.ModelAdmin):
    form = RadioStationForm

class SpeechAdmin(admin.ModelAdmin):
    form = SpeechForm

class PerformerAdmin(admin.ModelAdmin):
    form = PerformerForm

class ReferenceAdmin(admin.ModelAdmin):
    form = ReferenceForm

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Type)
admin.site.register(TypeBroadcasting)
admin.site.register(Speech, SpeechAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Performer, PerformerAdmin)
admin.site.register(Piece)
admin.site.register(Speaker)
admin.site.register(Author)
admin.site.register(RadioStation)
admin.site.register(PerformerType)
admin.site.register(AdditionalInfoLog)

class AdditionalInfoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change): 
        instance = form.save(commit=False)
        if instance.created_by is None:
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance

    def save_formset(self, request, form, formset, change): 
        def set_user(instance):
            if not instance.created_by:
                instance.created_by = request.user
            instance.save()

admin.site.register(AdditionalInfo, AdditionalInfoAdmin)

class CommentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
admin.site.register(Comment, CommentAdmin)

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('content', 'user')
    extra = 0

#class RadioDiffusionInline(admin.TabularInline):
#    model = Event.relates_to_radio.through
#    form = RadioDiffusionForm
#    exclude = ('relates_to_radio',)
#    fk_name = 'from_event'
#
class EventAdmin(ImportExportModelAdmin):
#    exclude = ('relates_to_radio',)
    exclude = ('bc_key', 'radio_station')
    form = EventForm
    resource_class = EventResource

    # the only way I found to increase width using suit+easy_select2
    def get_form(self, request, obj=None, **kwargs):
        form = super(EventAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['title'].widget.attrs['style'] = 'width: 520px;'
        return form

#    inlines = (CommentInline, )

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit=False)
        if instance.created_by is None:
            instance.created_by = request.user
        instance.edited_by = request.user
        instance.save()
        form.save_m2m()
        return instance

    def save_formset(self, request, form, formset, change): 

        def set_user(instance):
            if not instance.created_by:
                instance.created_by = request.user
            instance.edited_by = request.user
            instance.save()

        if formset.model == Article:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()

class BroadcastingAdmin(admin.ModelAdmin):
#    exclude = ('edited_by')
    form = BroadcastingForm

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit=False)
        if instance.created_by is None:
            instance.created_by = request.user
        instance.edited_by = request.user
        instance.save()
        form.save_m2m()
        return instance

    def save_formset(self, request, form, formset, change): 
        def set_user(instance):
            if not instance.created_by:
                instance.created_by = request.user
            instance.edited_by = request.user
            instance.save()

        if formset.model == Article:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()

admin.site.register(Event, EventAdmin)
admin.site.register(Broadcasting, BroadcastingAdmin)
