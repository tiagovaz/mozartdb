# -*- coding: utf-8 -*-

from django.contrib import admin
from django.forms import TextInput, Textarea
from easy_select2 import select2_modelform, select2_modelform_meta
#from mozartweb.forms import RadioDiffusionForm
from mozartweb.models import *
from django import forms
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ManyToManyWidget
from import_export import fields
from re import sub

# Export setup class
class EventResource(resources.ModelResource):
    title = fields.Field(column_name=Event._meta.get_field_by_name('title')[0].verbose_name)
    type__type = fields.Field(column_name=Event._meta.get_field_by_name('type')[0].verbose_name)
    start_date = fields.Field(column_name=Event._meta.get_field_by_name('start_date')[0].verbose_name)
    end_date = fields.Field(column_name=Event._meta.get_field_by_name('end_date')[0].verbose_name)
    places = fields.Field(column_name=Event._meta.get_field_by_name('places')[0].verbose_name)
    piece = fields.Field(column_name=Event._meta.get_field_by_name('piece')[0].verbose_name)
    performer = fields.Field(column_name=Event._meta.get_field_by_name('performer')[0].verbose_name)
    speech = fields.Field(column_name=Event._meta.get_field_by_name('speech')[0].verbose_name)
    relates_to_broadcasting = fields.Field(column_name=Event._meta.get_field_by_name('relates_to_broadcasting')[0].verbose_name)
    radio_station__name = fields.Field(column_name=Event._meta.get_field_by_name('radio_station')[0].verbose_name)
    comments = fields.Field(column_name=Comment._meta.get_field_by_name('content')[0].verbose_name)
    info = fields.Field(column_name=AdditionalInfo._meta.get_field_by_name('content')[0].verbose_name)

    def dehydrate_title(self, event):
        return sub('<[^<]+?>', '', event.title)

    def dehydrate_start_date(self, event):
        return event.format_start_date()

    def dehydrate_end_date(self, event):
        return event.format_end_date()

    def dehydrate_created_by(self, event):
        return event.created_by.__str__()

    def dehydrate_edited_by(self, event):
        return event.edited_by.__str__()

    def dehydrate_performer(self, event):
        performers = []
        for p in event.performer.all():
            performers.append(p.__str__())
        return "; ".join(performers)

    def dehydrate_reference(self, event):
        references = []
        for p in event.reference.all():
            references.append(p.__str__())
        return "; ".join(references)

    def dehydrate_speech(self, event):
        speechs = []
        for p in event.speech.all():
            speechs.append(p.__str__())
        return "; ".join(speechs)

    def dehydrate_piece(self, event):
        pieces = []
        for p in event.piece.all():
            pieces.append(p.__str__())
        return "; ".join(pieces)

    def dehydrate_places(self, event):
        places = []
        for p in event.places.all():
            places.append(p.__str__())
        return "; ".join(places)

    def dehydrate_relates_to_broadcasting(self, event):
        bs = []
        for p in event.relates_to_broadcasting.all():
            bs.append(p.__str__())
        text = "; ".join(bs)
        return sub('<[^<]+?>', '', text)

    def dehydrate_info(self, event):
        info_list = []
        for i in event.get_info():
            info_list.append(i.__str__())
        text = "; ".join(info_list)
        return sub('<[^<]+?>', '', text)

    def dehydrate_comments(self, event):
        c_list = []
        for c in event.get_comments():
            c_list.append(c.__str__())
        return "; ".join(c_list)

    class Meta:
        export_order = ('id',
                  'title',
                  'type__type', 
                  'start_date', 
                  'end_date', 
                  'places', #
                  'piece', #
                  'performer',  #
                  'speech',  #
                  'relates_to_broadcasting', #
                  'radio_station__name', 
                  'comments', #
                  'info', #
                 )

        fields = ('id',
                  'title',
                  'places',
                  'radio_station__name', 
                  'type__type', 
                  'performer',  #
                  'speech',  #
                  'piece', #
                  'start_date', 
                  'end_date', 
                  'relates_to_broadcasting', #
                  'comments', #
                  'info', #
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
JournalForm = select2_modelform(Journal)

class PlaceAdmin(admin.ModelAdmin):
    list_max_show_all = 10000
    form = PlaceForm

class RadioStationAdmin(admin.ModelAdmin):
    form = RadioStationForm

class SpeechAdmin(admin.ModelAdmin):
    list_max_show_all = 10000
    form = SpeechForm

class PerformerAdmin(admin.ModelAdmin):
    list_max_show_all = 10000
    form = PerformerForm

class JournalAdmin(admin.ModelAdmin):
    list_max_show_all = 10000
    form = JournalForm

class ReferenceAdmin(admin.ModelAdmin):
    list_max_show_all = 10000
    form = ReferenceForm

class PieceAdmin(admin.ModelAdmin):
    list_max_show_all = 10000

class TypeAdmin(admin.ModelAdmin):
    list_max_show_all = 10000

class AdditionalInfoLogAdmin(admin.ModelAdmin):
    list_max_show_all = 10000

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Type, TypeAdmin)
admin.site.register(TypeBroadcasting)
admin.site.register(Speech, SpeechAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Performer, PerformerAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Speaker)
admin.site.register(Author)
admin.site.register(RadioStation)
admin.site.register(PerformerType)
admin.site.register(AdditionalInfoLog, AdditionalInfoLogAdmin)

class AdditionalInfoAdmin(admin.ModelAdmin):
    list_max_show_all = 10000
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
    list_max_show_all = 10000
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
    list_max_show_all = 10000
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
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
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
