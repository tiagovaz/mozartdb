from django.contrib import admin
from django.forms import TextInput, Textarea
from easy_select2 import select2_modelform, select2_modelform_meta
#from mozartweb.forms import RadioDiffusionForm
from mozartweb.models import City, Country, Type, TypeBroadcasting, Speech, Reference, Place, Performer, Piece, Speaker, RadioStation, PerformerType, Comment, Event, Broadcasting, Author
from django import forms

#from forms import *

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
class EventAdmin(admin.ModelAdmin):
#    exclude = ('relates_to_radio',)
    exclude = ('bc_key', 'radio_station')
    form = EventForm

    # the only way I found to increase width using suit+easy_select2
    def get_form(self, request, obj=None, **kwargs):
        form = super(EventAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['title'].widget.attrs['style'] = 'width: 520px;'
        return form

#    inlines = (CommentInline, )

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit=False)
        if instance.created_by is None:
#        if not hasattr(instance,'created_by'):
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
